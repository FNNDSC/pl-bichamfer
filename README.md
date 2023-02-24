# Radial Distance Map

[![Version](https://img.shields.io/docker/v/fnndsc/pl-bichamfer?sort=semver)](https://hub.docker.com/r/fnndsc/pl-bichamfer)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-bichamfer)](https://github.com/FNNDSC/pl-bichamfer/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-bichamfer/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-bichamfer/actions/workflows/ci.yml)

`pl-bichamfer` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin wrapper around a bi-directional `mincchamfer` program.
It creates a radial distance map for every MINC mask image inside a
given input directory.

## Installation

`pl-bichamfer` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://raw.githubusercontent.com/FNNDSC/ChRIS_store_ui/963938c241636e4c3dc4753ee1327f56cb82d8b5/src/assets/public/badges/light.svg)](https://chrisstore.co/plugin/pl-bichamfer)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-bichamfer` as a container.
To print its available options, run:

```shell
apptainer exec docker://fnndsc/pl-bichamfer bichamfer --help
```

## Examples

Convert a directory containing .mnc mask images to distance map volumes,
where output files use the same file names as their corresponding files:

```shell
apptainer exec docker://fnndsc/pl-bichamfer bichamfer input_masks/ output_chamfers/
```

If the input directory is the same as the output directory, then output file
names are renamed to have the suffix `.chamfer.mnc`. This is useful for running
`pl-bichamfer` "in-place" on all masks in the current working directory:

```shell
apptainer exec docker://fnndsc/pl-bichamfer bichamfer . .
```
