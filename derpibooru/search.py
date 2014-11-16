# -*- coding: utf-8 -*-

# Copyright (c) 2014, Joshua Stone
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from sys import version_info

from .request import get_images, url
from .image import Image
from .helpers import tags, api_key, sort_format, join_params

__all__ = [
  "Search"
]

class Search(object):
  """
  Search() is the primary interface for interacting with Derpibooru's REST API.

  All properties are read-only, and every method returns a new instance of
  Search() to avoid mutating state in ongoing search queries. This makes object
  interactions predictable as well as making versioning of searches relatively
  easy.
  """
  def __init__(self, key="", q={}, sf="created_at", sd="desc", limit=50,
               faves="", upvotes="", uploads="", watched=""):
    """
    By default initializes an instance of Search with the parameters to get
    the first 50 images on Derpibooru's front page
    """
    self._params = {
      "key": api_key(key),
      "q": tags(q),
      "sf": sort_format(sf),
      "sd": sd,
      "faves": faves,
      "upvotes": upvotes,
      "uploads": uploads,
      "watched": watched
    }
    self._limit = limit
    self._search = get_images(self.parameters, self.limit)
  
  def __iter__(self):
    """
    Make Search() iterable so that new search results can be lazily generated
    for performance reasons
    """
    return self

  @property
  def parameters(self):
    """
    Returns a list of available parameters; useful for passing stating to new
    instances of Search()
    """
    return self._params

  @property
  def key(self):
    """
    Returns a string of the current API key in use; by default is empty
    """
    return self.parameters["key"]    

  @property
  def q(self):
    """
    Returns a set of strings representing a search query; by default is empty
    """
    return self.parameters["q"]

  @property
  def sf(self):
    """
    Returns the current sort format; by default uses `created_at' for newest to
    oldest posts
    """
    return self.parameters["sf"]

  @property
  def sd(self):
    """
    Returns current sorting direction; by default uses `descending' for biggest
    to smallest based on the current sorting format
    """
    return self.parameters["sd"]

  @property
  def limit(self):
    """
    Returns the current limit set for image results; default is 50 so as to be
    less of a burden on Derpibooru
    """
    return self._limit

  @property
  def url(self):
    """
    Returns a search URL built on set parameters. Example based on default
    parameters:

    https://derpiboo.ru/search?sd=desc&sf=created_at&q=%2A
    """
    return url(self.parameters)

  def api_key(self, key=""):
    """
    Takes a user's API key string which applies content settings. API keys can
    be found at <https://derpiboo.ru/users/edit>
    """
    params = join_params(self.parameters, {"key": key, "limit": self.limit})

    return self.__class__(**params)

  def query(self, *q):
    """
    Takes one or more strings for searching by tag and/or metadata
    """
    params = join_params(self.parameters, {"q": q, "limit": self.limit})

    return self.__class__(**params)

  def sort_by(self, sf):
    """
    Determines how to sort search results; default is sort.creation_date
    """
    params = join_params(self.parameters, {"sf": sf, "limit": self.limit})

    return self.__class__(**params)

  def descending(self):
    """
    Order results from largest to smallest; default is descending order
    """
    params = join_params(self.parameters, {"sd": "desc", "limit": self.limit})

    return self.__class__(**params)

  def ascending(self):
    """
    Order results from smallest to largest; default is descending order
    """
    params = join_params(self.parameters, {"sd": "asc", "limit": self.limit})

    return self.__class__(**new_params)

  def image_limit(self, limit):
    """
    Set absolute limit on number of images to return, or set to None to return
    as many results as needed; default 50 images
    """
    params = join_params(self.parameters, {"limit": limit})
    print(params)
    return self.__class__(**params)

  def faves(self, option):
    params = join_params(self.parameters, {"faves": option, "limit": self.limit})

    return self.__class__(**params)

  def upvotes(self, option):
    params = join_params(self.parameters, {"upvotes": option, "limit": self.limit})

    return self.__class__(**params)

  def uploads(self, option):
    params = join_params(self.parameters, {"uploads": option, "limit": self.limit})

    return self.__class__(**params)

  def watched(self, option):
    params = join_params(self.parameters, {"watched": option, "limit": self.limit})

    return self.__class__(**params)

if version_info < (3, 0):
  def next(self):
    """
    Returns a result wrapped in a new instance of Image()
    """
    return Image(self._search.next())

  Search.next = next

else:
  def __next__(self):
    """
    Returns a result wrapped in a new instance of Image()
    """
    return Image(next(self._search))

  Search.__next__ = __next__

