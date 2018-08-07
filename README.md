# whratio

[![PyPI downloads](http://pepy.tech/badge/whratio)](https://pepy.tech/project/whratio)
[![PyPI version](https://img.shields.io/pypi/v/whratio.svg)](https://pypi.python.org/pypi/whratio)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/whratio.svg)](https://pypi.python.org/pypi/whratio)

Calculate integer and decimal aspect ratio for dimensions.

## CLI examples

```sh
    $ whratio 1024 768
    4 3 1.33
```

```sh
    $ whratio -d -n6 256 196
    1.306122
```

```sh
    whratio -WH 2560 1080 | tr " " :
    64:27
```

## Python package examples

```python3
    >>> from whratio import ratio

    >>> ratio.as_int(1920, 1080)
    (16, 9)

    >>> ratio.as_float(1920, 1080)
    1.77

    >>> ratio.as_float(1920, 1080, ndigits=4)
    1.7778
```

## Installation

Using [pip](https://pip.pypa.io/en/stable/installing/):

```sh
    # pip3 install whratio
```
