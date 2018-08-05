"""whratio setuptools file"""

from setuptools import setup
import whratio as info

setup(
    name        = info.PKG_NAME,
    version     = info.__version__,
    description = info.__doc__,

    author       = info.__author__,
    author_email = info.__email__,
    license      = info.__license__,

    keywords = "calculate aspect ratio dimension width height image video",
    url      = "https://github.com/mirukan/%s" % info.PKG_NAME,

    py_modules   = [info.PKG_NAME],
    entry_points = {
        "console_scripts": [
            "%s=%s:main" % (info.PKG_NAME, info.PKG_NAME)
        ]
    },

    classifiers=[
        "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",

        "Environment :: Console",

        "Topic :: Utilities",

        ("License :: OSI Approved :: "
         "GNU Lesser General Public License v3 or later (LGPLv3+)"),

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",

        "Natural Language :: English",

        "Operating System :: POSIX",
    ]
)
