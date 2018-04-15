# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Calculate integer and decimal aspect ratio for dimensions."""

from __future__ import print_function

import sys
import textwrap

__author__  = "ccc032"
__license__ = "GPLv3"
__version__ = "1.1.0"
__email__   = "ym96@protonmail.ch"


def ratio_float(width, height, ndigits=2):
    return round(width / height, ndigits)


def ratio_int(width, height):
    gcd = get_gcd(width, height)
    return int(width / gcd), int(height / gcd)


def get_gcd(a, b):
    while a:
        a, b = b % a, a
    return b


def main():
    """
    Usage: whratio <width> <height>
    Print integer and decimal aspect ratio for the <width> and <height>.

    Options:

      -h, --help
        Show this help.

    Examples:

      whratio 1024 768
        Returns "4 3 1.33" (integer 4:3, decimal 1.33).

      whratio 2560 1080
        Returns "64 27 2.37" (Also wrongly called "21:9").

      whratio.py 100 200 | cut -d' ' -f3
        Get the 3rd value of "1 2 0.5" (decimal ratio 0.5) on POSIX systems."""

    try:
        if sys.argv[1] in ("-h", "--help"):
            print(textwrap.dedent(main.__doc__))
            sys.exit()
    except IndexError:
        print(textwrap.dedent(main.__doc__))
        sys.exit(1)

    try:
        width  = float(sys.argv[1])
        height = float(sys.argv[2])
    except (IndexError, ValueError):
        raise TypeError("Need two number arguments, width and height.")

    int_w, int_h = ratio_int(width, height)
    print(int_w, int_h, ratio_float(width, height))


if __name__ == "__main__":
    main()
