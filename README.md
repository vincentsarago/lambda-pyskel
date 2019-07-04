# lambda-pyskel

Create python AWS Lambda skeleton from templates.

[![Packaging status](https://badge.fury.io/py/lambda-pyskel.svg)](https://badge.fury.io/py/lambda-pyskel)
[![CircleCI](https://circleci.com/gh/vincentsarago/lambda-pyskel.svg?style=svg)](https://circleci.com/gh/vincentsarago/lambda-pyskel)
[![codecov](https://codecov.io/gh/vincentsarago/lambda-pyskel/branch/master/graph/badge.svg)](https://codecov.io/gh/vincentsarago/lambda-pyskel)

Shameless inspiration from @sgillies https://github.com/mapbox/pyskel

## Install

You can install lambda-pyskel using pip

```bash
$ pip install -U pip
$ pip install lambda-pyskel
```

or install from source:

```bash
$ git clone https://github.com/vincentsarago/lambda-pyskel.git
$ cd lambda-pyskel
$ pip install -U pip
$ pip install -e .
```

## Templates

**Three** different templates are available:
  - **simple**: simple python lambda function
  - **rasterio**: include rasterio wheels
  - **gdal**: include custom gdal (2.4.1) installation [from remotepixel docker image](https://github.com/RemotePixel/amazonlinux-gdal)

Each templates has the following structure::
```
pyskel/                : main module
    __init__.py
    handler.py         : handler function
tests/                 : python tests
    test_handler.py
    test_mod.py
Dockerfile             : Dockerfile to create the package.zip
LICENSE                : BSD-2 license file
Makefile               : make commands to create/tests the packages
README.md             : Readme
setup.py               : Python setup
tox.ini                : tox template
```

## Deployement Toolkit

In addition to python module templates, lambda-pyskel can also add
configuration files for **serverless** or **kes** toolkit.

**kes**: http://devseed.com/kes/

**serverless**: https://serverless.com

## Usage

```bash
$ lps --help
Usage: lps [OPTIONS] NAME

  Create new python AWS Lambda skeleton.

Options:
  --version                             Show the version and exit.
  --template [simple|rasterio|gdal]     Use specific template (default: 'simple')
  --serverless-toolkit [kes|serverless] Add deployement toolkit
  --help                                Show this message and exit.
```

Create a python lambda function with rasterio

```bash
$ lps yo --template rasterio
$ ls -1 yo
  Dockerfile
  LICENSE
  Makefile
  README.rst
  setup.py
  tests/
  tox.ini
  yo/

# edit yo/handler.py and setup.py
$ make build
```

## Contribution & Devellopement

Issues and pull requests are more than welcome.

**Dev install & Pull-Request**

```bash
$ git clone https://github.com/vincentsarago/lambda-pyskel.git
$ cd lambda-pyskel
$ pip install -e .[dev]
```

*Python3.6 only*

This repo is set to use `pre-commit` to run *flake8*, *pydocstring* and *black* ("uncompromising Python code formatter") when committing new code.

```
$ pre-commit install
$ git add .
$ git commit -m'my change'
black....................................................................Passed
Flake8...................................................................Passed
Verifying PEP257 Compliance..............................................Passed
$ git push origin
```