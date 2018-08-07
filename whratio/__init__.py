# Copyright 2018 miruka
# This file is part of whratio, licensed under LGPLv3.

import signal
import sys

from . import __about__

__doc__ = __about__.__doc__


def die(sig_nbr=0, _=None):
    """Exit on process signal without traceback"""
    sys.exit(128 + sig_nbr)


for sig in ("HUP", "INT", "QUIT", "TERM"):
    signal.signal(getattr(signal, f"SIG{sig}"), die)
