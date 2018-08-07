# Copyright 2018 miruka
# This file is part of whratio, licensed under LGPLv3.

import signal
import sys
import warnings

from . import __about__, ratio

__doc__ = __about__.__doc__

warnings.simplefilter('always', DeprecationWarning)


def ratio_int(*args, **kwargs):
    warnings.warn("Replaced in >=v2.0.0, use whratio.ratio.as_int instead.",
                  DeprecationWarning)
    return ratio.as_int(*args, **kwargs)


def ratio_float(*args, **kwargs):
    warnings.warn("Replaced in >=v2.0.0, use whratio.ratio.as_float instead.",
                  DeprecationWarning)
    return ratio.as_float(*args, **kwargs)


def _die(sig_num, **_):
    """Exit on process signal without traceback"""
    sys.exit(128 + sig_num)


try:
    for sig in ("HUP", "INT", "QUIT", "TERM"):
        signal.signal(getattr(signal, f"SIG{sig}"), _die)
except ValueError:  # We're imported from a thread
    pass
