"""whratio setuptools file"""

from setuptools import setup, find_packages
import whratio

setup(
    name     = whratio.__name__,
    version  = whratio.__version__,
    packages = find_packages(),
    scripts  = ["whratio.py"],

    author       = whratio.__author__,
    author_email = whratio.__email__,
    description  = whratio.__doc__,
    license      = whratio.__license__,
    keywords     = "calculate aspect ratio dimension width height image video",
    url          = "https://github.com/ccc032/whratio",

    entry_points = {
        "console_scripts": [
            "whratio=whratio:main"
        ]
    }
)
