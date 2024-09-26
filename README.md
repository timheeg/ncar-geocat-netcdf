# NCAR GeoCAT example

This repo contains example that opens and animates global weather data from a
`NetCDF` file using NCAR `GeoCAT` and `xarray` libraries.

## Source Code

Adapted from:

* [GeoCAT > Getting Started > Basic
Examples](https://geocat-comp.readthedocs.io/en/stable/getting_started/mini-examples.html),
and
* [NCL animate
  example](https://geocat-examples.readthedocs.io/en/latest/gallery/Animations/NCL_animate_1.html#sphx-glr-gallery-animations-ncl-animate-1-py)

## Container setup and GeoCAT installation

Followed install documentation from project site at
<https://geocat-comp.readthedocs.io/en/stable/installation.html>

## Python formatting

The dev container has the VS Code extension `ms-python.black-formatter`
installed. Follow extension instructions to configure python files to format
using it.

## Source Data

The NetCDF file used in this example came from NCAR Research Data Archive (RDA) NCEP Global Forecast System (GFS) Analyses and Forecasts dataset, T170 resolution.

## Mount source data

The `SOURCE_DATA` environment variable defines the location of source data on
the local machine.

⚠️ You must define the `SOURCE_DATA` environment variable.

> Since I run code from within a development WSL image, my personal local folder
containing various example data files is available via `/mnt/c`.

The dev container mounts that data folder to `/var/data` inside the container.

For example, data is available like this.

```bash
ls -lah /var/data/ncar-rda/d084006/T170/20070821_T170_1.nc
```

## Virtual environment

The container creates a conda environment named `geocat` for development,
`source activate geocat`.

## Basic animation

The `basic-animate.py` script crashes with an index out of range exception when
saving the gif animation to a file. Not sure why yet. Regardless, the gif does
get created.

Run with `python basic-animate.py`.

The script will output `animate_1.git`.
