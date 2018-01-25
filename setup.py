#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
  name = "DerPyBooru",
  description = "Python bindings for Derpibooru's API",
  url = "https://github.com/joshua-stone/DerPyBooru",
  version = "0.7.2",
  author = "Joshua Stone",
  author_email = "joshua.gage.stone@gmail.com",
  license = "Simplified BSD License",
  platforms = ["any"],
  packages = find_packages(),
  install_requires = ["requests"],
  include_package_data = True,
  download_url = "https://github.com/joshua-stone/DerPyBooru/tarball/0.7.2",
  classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: BSD License",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3"
  ]
)
