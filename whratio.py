# Copyright 2018 miruka

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Calculate integer and decimal aspect ratio for dimensions."""

from __future__ import print_function

import inspect

import docopt

PKG_NAME    = "whratio"
__version__ = "1.1.2"
__author__  = "miruka"
__email__   = "miruka@disroot.org"
__license__ = "LGPLv3"


def ratio_float(width, height, ndigits=2):
    """Return a decimal ratio like 1.78"""
    return round(width / height, ndigits)


def ratio_int(width, height):
    """Return an integer ratio tuple like (16, 9)"""
    gcd = get_gcd(width, height)
    return int(width / gcd), int(height / gcd)


def get_gcd(a, b):
    """Return greatest common divisor for a and b"""
    while a:
        a, b = b % a, a
    return b


def main():
    """Usage: <NAME> WIDTH HEIGHT

    Print integer and decimal aspect ratio for the given numbers.

    Arguments:
      WIDTH   Width to calculate ratio for.
      HEIGHT  Height to calculate ratio for.

    Options:
      -h, --help     Show this help.
      -V, --version  Show the program's version.

    Examples:
      <NAME> 1024 768
        Return "4 3 1.33" (integer 4:3, decimal 1.33).

      <NAME> 2560 1080
        Return "64 27 2.37" (Also wrongly called "21:9").

      <NAME> 100 200 | cut -d' ' -f3
        Get the 3rd value of "1 2 0.5" (decimal ratio 0.5) on POSIX systems.
    """
    doc  = inspect.cleandoc(main.__doc__).replace("<NAME>", PKG_NAME)
    args = docopt.docopt(doc, version=__version__)

    width  = float(args["WIDTH"])
    height = float(args["HEIGHT"])

    int_w, int_h = ratio_int(width, height)
    print(int_w, int_h, ratio_float(width, height))


if __name__ == "__main__":
    main()
