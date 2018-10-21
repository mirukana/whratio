#!/usr/bin/env python3
# Copyright 2018 miruka
# This file is part of whratio, licensed under LGPLv3.

"Ratio calculation functions."


def get_gcd(a, b):
    "Return greatest common divisor for a and b."
    while a:
        a, b = b % a, a
    return b


def as_int(width, height):
    "Return an integer ratio tuple like (16, 9)."
    gcd = get_gcd(width, height)
    return int(width / gcd), int(height / gcd)


def as_float(width, height):
    "Return a decimal ratio like 1.7777...."
    return width / height
