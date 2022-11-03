<div align="center">

<img width="150px" src="https://raw.githubusercontent.com/AjinkyaIndulkar/pkgviz-python/main/assets/logo.png" alt="logo" style="padding-top:50px;padding-bottom:50px">

<h1> pkgviz-python </h1>

Framework to visualise python packages.

[![license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/AjinkyaIndulkar/pkgviz-python/dot/blob/main/LICENSE)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3106/)
[![PyPI version](https://badge.fury.io/py/pkgviz-python.svg)](https://badge.fury.io/py/pkgviz-python)
[![Code Check](https://github.com/AjinkyaIndulkar/pkgviz-python/actions/workflows/code-check.yaml/badge.svg)](https://github.com/AjinkyaIndulkar/pkgviz-python/actions/workflows/code-check.yaml)
[![CI](https://github.com/AjinkyaIndulkar/pkgviz-python/actions/workflows/pkgviz-ci.yaml/badge.svg)](https://github.com/AjinkyaIndulkar/pkgviz-python/actions/workflows/pkgviz-ci.yaml)

</div>

## Getting Started

### Pre-requisites:

The package uses `graphviz` as a dependency. You will need to install the required binaries for it.

-   Linux: `sudo apt install graphviz`
-   MacOS: `brew install graphviz`

Refer to https://graphviz.org/download/ for more installation options.

**Note**: It is recommended to setup a virtual environment of your choice before installing the package.

### Install from PyPI:

```
pip install pkgviz-python
```

### Install from source:

```
git clone https://github.com/AjinkyaIndulkar/pkgviz-python
cd pkgviz-python
pip install .
```

## CLI Usage

Run the following command to generate a graph visualisation of the `math` package:

```
pkgviz -p math -o output/viz.svg
```

The above command should generate an SVG output as below:

<div align="center">

<img width="600px" src="https://raw.githubusercontent.com/AjinkyaIndulkar/pkgviz-python/main/assets/viz-demo.svg" alt="demo-viz" style="padding-top:50px;padding-bottom:50px">

</div>
