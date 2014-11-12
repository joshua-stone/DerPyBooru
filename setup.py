#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

import derpibooru

setup(
  name = "DerPyBooru",
  url = "https://github.com/joshua-stone/DerPyBooru",
  version = "0.3",
  author = "Joshua Stone",
  license = "Simplified BSD License",
  platforms = ["any"],
  packages = find_packages(),
  include_package_data = True,
  classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Simplified BSD License",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Internet"
  ]
)
