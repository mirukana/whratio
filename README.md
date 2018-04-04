# whratio

Calculate integer and decimal aspect ratio for dimensions.

## Python module usage example

    >>> from whratio import *

    >>> ratio_float(640, 480)
    1.33

    >>> ratio_float(1920, 1080, ndigits=4)
    1.7778

    >>> ratio_int(1920, 1080)
    (16, 9)

## CLI Usage

    whratio [-h|--help] <width> <height>

### Examples

    whratio 1024 768

Returns `4 3 1.33` (integer *4:3*, decimal *1.33*).

    whratio 2560 1080

Returns `64 27 2.37` (Also wrongly called "21:9").

    whratio.py 100 200 | cut -d' ' -f3

Get the 3rd value of `1 2 0.5` (decimal ratio *0.5*) on POSIX systems.

## Installation

Requires Python 2 or 3.

From **pip**:

    sudo pip install whratio

Manually:

    git clone https://github.com/ccc032/whratio
    cd whratio
    sudo python setup.py install
