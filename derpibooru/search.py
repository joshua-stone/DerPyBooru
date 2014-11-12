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
from .helpers import tags, api_key, sort_format

__all__ = [
  "Search"
]

class Search(object):
  def __init__(self, key="", q={}, sf="created_at", sd="desc", limit=50):
    self._params = {
      "key": api_key(key),
      "q": tags(q),
      "sf": sort_format(sf),
      "sd": sd,
      "limit": limit
    }

    self._search = get_images(**self.parameters)
  
  def __iter__(self):
    return self

  @property
  def parameters(self):
    return self._params

  @property
  def key(self):
    return self.parameters["key"]    

  @property
  def q(self):
    return self.parameters["q"]

  @property
  def sf(self):
    return self.parameters["sf"]

  @property
  def sd(self):
    return self.parameters["sd"]

  @property
  def limit(self):
    return self.parameters["limit"]

  @property
  def url(self):
    params = {
      "key": self.key,
      "q": self.q,
      "sf": self.sf,
      "sd": self.sd,
    }

    return url(params)

  def api_key(self, key=None):
    return self.__class__(key, self.q, self.sf, self.sd, self.limit)

  def query(self, *q):
    return self.__class__(self.key, q, self.sf, self.sd, self.limit)

  def sort_by(self, sf):
    return self.__class__(self.key, self.q, sf, self.sd, self.limit)

  def descending(self):
    return self.__class__(self.key, self.q, self.sf, "desc", self.limit)

  def ascending(self):
    return self.__class__(self.key, self.q, self.sf, "asc", self.limit)

  def image_limit(self, limit):
    return self.__class__(self.key, self.q, self.sf, self.sd, limit)

if version_info < (3, 0):
  def next(self):
    return self._search.next()

  Search.next = next

else:
  def __next__(self):
    return next(self._search)

  Search.__next__ = __next__

