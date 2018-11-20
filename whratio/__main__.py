#!/usr/bin/env python3
# Copyright 2018 miruka
# This file is part of whratio, licensed under LGPLv3.

"""Usage: whratio [options] WIDTH HEIGHT

Print aspect ratio for the given numbers, integer and decimal by default.

Arguments:
  WIDTH   Width to calculate ratio for.
  HEIGHT  Height to calculate ratio for.

Options:
  -W, --int-width        Print the integer ratio width.
  -H, --int-height       Print the integer ratio height.
  -d, --decimal          Print the decimal ratio.
  -n NUM, --ndigits NUM  Round decimal ratio to NUM numbers.

  -h, --help     Show this help.
  -V, --version  Show the program version."""

import sys

import docopt
import colorama
from colorama import Fore

from . import __about__, as_float, as_int

colorama.init()


def main():
    "Process CLI arguments and call appropriate functions."
    try:
        args = docopt.docopt(__doc__, version=__about__.__version__)
    except docopt.DocoptExit:
        if len(sys.argv) > 1:
            print(f"{Fore.RED}Invalid command syntax, "
                  f"check help:{Fore.RESET}\n")
        print(__doc__)
        sys.exit(1)

    print_all = False
    if not (args["--int-width"] or args["--int-height"] or args["--decimal"]):
        print_all = True

    width    = float(args["WIDTH"])
    height   = float(args["HEIGHT"])

    as_int_   = as_int(width, height)
    as_float_ = as_float(width, height)

    if args["--ndigits"]:
        as_float_ = round(as_float_, int(args["--ndigits"]))

    to_print = []

    if args["--int-width"] or print_all:
        to_print.append(f"{Fore.BLUE}{as_int_[0]!s}")

    if args["--int-height"] or print_all:
        to_print.append(f"{Fore.BLUE}{as_int_[1]!s}")

    if args["--decimal"] or print_all:
        to_print.append(f"{Fore.MAGENTA}{as_float_!s}")

    print(" ".join(to_print))


if __name__ == "__main__":
    main()
