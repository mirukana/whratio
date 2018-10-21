# whratio

[![PyPI downloads](http://pepy.tech/badge/whratio)](https://pepy.tech/project/whratio)
[![PyPI version](https://img.shields.io/pypi/v/whratio.svg)](https://pypi.python.org/pypi/whratio)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/whratio.svg)](https://pypi.python.org/pypi/whratio)

Calculate integer and decimal aspect ratio for dimensions.

## CLI examples

```sh
    $ whratio 1024 768
    4 3 1.3333333333333333
```

```sh
    $ whratio -d -n 2 256 196
    1.31
```

```sh
    whratio -WH 2560 1080 | tr " " :
    64:27
```

## Python package examples

```python3
    >>> import whratio

    >>> whratio.as_int(1920, 1080)
    (16, 9)

    >>> whratio.as_float(1920, 1080)
    1.7777777777777777

    >>> round(whratio.as_float(1920, 1080), 2)
    1.78
```

## Installation

Using [pip](https://pip.pypa.io/en/stable/installing/):

```sh
    # pip3 install whratio
```
