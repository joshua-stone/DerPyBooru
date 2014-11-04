#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

import derpibooru

setup(
  name = "PyDerpibooru",
  summary = "Python wrapper for Derpibooru's API",
  url = "https://github.com/joshua-stone/pyderpibooru",
  version = "0.1",
  author = "Joshua Stone",
  email = "joshua.gage.stone@gmail.com",
  license = "Simplified BSD License",
  copyright = "Copyright 2014 Joshua Stone",
  platforms = ["any"],
  include_package_data = True,
  classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet"
  ]
)
