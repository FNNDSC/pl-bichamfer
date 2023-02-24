# Radial Distance Map

[![Version](https://img.shields.io/docker/v/fnndsc/pl-radial-distance-map?sort=semver)](https://hub.docker.com/r/fnndsc/pl-radial-distance-map)
[![MIT License](https://img.shields.io/github/license/fnndsc/pl-radial-distance-map)](https://github.com/FNNDSC/pl-radial-distance-map/blob/main/LICENSE)
[![ci](https://github.com/FNNDSC/pl-radial-distance-map/actions/workflows/ci.yml/badge.svg)](https://github.com/FNNDSC/pl-radial-distance-map/actions/workflows/ci.yml)

`pl-radial-distance-map` is a [_ChRIS_](https://chrisproject.org/)
_ds_ plugin wrapper around a bi-directional `mincchamfer` program.
It creates a radial distance map for every MINC mask image inside a
given input directory.

## Installation

`pl-radial-distance-map` is a _[ChRIS](https://chrisproject.org/) plugin_, meaning it can
run from either within _ChRIS_ or the command-line.

[![Get it from chrisstore.co](https://raw.githubusercontent.com/FNNDSC/ChRIS_store_ui/963938c241636e4c3dc4753ee1327f56cb82d8b5/src/assets/public/badges/light.svg)](https://chrisstore.co/plugin/pl-radial-distance-map)

## Local Usage

To get started with local command-line usage, use [Apptainer](https://apptainer.org/)
(a.k.a. Singularity) to run `pl-radial-distance-map` as a container.
To print its available options, run:

```shell
apptainer exec docker://fnndsc/pl-radial-distance-map bichamfer --help
```

## Examples

Convert a directory containing .mnc mask images to distance map volumes,
where output files use the same file names as their corresponding files:

```shell
apptainer exec docker://fnndsc/pl-radial-distance-map bichamfer input_masks/ output_chamfers/
```

If the input directory is the same as the output directory, then output file
names are renamed to have the suffix `.chamfer.mnc`. This is useful for running
`pl-radial-distance-map` "in-place" on all masks in the current working directory:

```shell
apptainer exec docker://fnndsc/pl-radial-distance-map bichamfer . .
```
