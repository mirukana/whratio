# Copyright 2018 miruka
# This file is part of whratio, licensed under LGPLv3.

"""whratio setuptools file"""

from setuptools import setup, find_packages

from whratio import __about__


def get_readme():
    with open("README.md", "r") as readme:
        return readme.read()


setup(
    name        = __about__.__pkg_name__,
    version     = __about__.__version__,

    author       = __about__.__author__,
    author_email = __about__.__email__,
    license      = __about__.__license__,

    description                   = __about__.__doc__,
    long_description              = get_readme(),
    long_description_content_type = "text/markdown",

    python_requires  = ">=3.5, <4",
    install_requires = [
        "docopt",
        "blessings"
    ],

    py_modules      = find_packages(),
    entry_points    = {
        "console_scripts": [
            "{0}={0}.__main__:main".format(__about__.__pkg_name__)
        ]
    },

    keywords = "calculate aspect ratio dimension width height image video",
    url      = f"https://github.com/mirukan/whratio",

    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",

        "Environment :: Console",

        "Topic :: Utilities",

        ("License :: OSI Approved :: "
         "GNU Lesser General Public License v3 or later (LGPLv3+)"),

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",

        "Natural Language :: English",

        "Operating System :: POSIX",
    ]
)
