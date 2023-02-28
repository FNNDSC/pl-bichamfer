#!/usr/bin/env python
import itertools
import os
import shlex
import subprocess as sp
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from chris_plugin import chris_plugin, PathMapper
from loguru import logger

__version__ = '1.0.1'

DISPLAY_TITLE = r"""
       _        _     _      _                      __          
      | |      | |   (_)    | |                    / _|         
 _ __ | |______| |__  _  ___| |__   __ _ _ __ ___ | |_ ___ _ __ 
| '_ \| |______| '_ \| |/ __| '_ \ / _` | '_ ` _ \|  _/ _ \ '__|
| |_) | |      | |_) | | (__| | | | (_| | | | | | | ||  __/ |   
| .__/|_|      |_.__/|_|\___|_| |_|\__,_|_| |_| |_|_| \___|_|   
| |
|_|
"""


parser = ArgumentParser(description='Create radial distance maps of masks using mincchamfer',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', '--pattern', default='**/*.mnc', type=str,
                    help='input file filter glob')
parser.add_argument('-b', '--boundary', default=10.0, type=float,
                    help='boundary distance 0 value')
parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')


@chris_plugin(
    parser=parser,
    title='Radial Distance Map',
    category='MRI Processing',
    min_memory_limit='1Gi',
    min_cpu_limit='1000m',
    min_gpu_limit=0
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    print(DISPLAY_TITLE, flush=True)

    # if output directory is the same as input directory,
    # then it's necessary to rename output files.
    mo = {}
    if inputdir == outputdir:
        mo['suffix'] = '.chamfer.mnc'
    mapper = PathMapper.file_mapper(inputdir, outputdir, glob=options.pattern, **mo)
    input_files, output_files = zip(*mapper)

    proc = len(os.sched_getaffinity(0))
    logger.debug('Using {} threads', proc)

    with ThreadPoolExecutor(max_workers=proc) as pool:
        results = pool.map(bichamfer, input_files, output_files, itertools.repeat(options.boundary))

    # raise any exceptions which occurred
    for _ in results:
        pass


def bichamfer(mask: os.PathLike, chamfer: os.PathLike, boundary: float):
    cmd = ('chamfer.sh', '-c', str(boundary), mask, chamfer)
    logger.info(shlex.join(map(str, cmd)))
    sp.run(cmd, check=True)


if __name__ == '__main__':
    main()
