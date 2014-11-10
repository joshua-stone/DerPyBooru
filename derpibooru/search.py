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

from .request import request, url

__all__ = [
  "Search"
]

class Search(object):
  def __init__(self, key=None, q={}, sf="created_at", sd="desc"):
    self._parameters = {
      "key": key,
      "q": {str(tag).strip() for tag in q if tag},
      "sf": sf,
      "sd": sd
    }
    self._search = request(self.parameters)
  
  def __iter__(self):
    return self

  @property
  def parameters(self):
    return self._parameters

  @property
  def url(self):
    return url(self._parameters)

  def key(self, key=None):
    self._parameters["key"] = key
    return Search(**self._parameters)

  def query(self, *q):
    self._parameters["q"] = {str(tag).strip() for tag in q if tag}
    return Search(**self._parameters)

  def descending(self):
    self._parameters["sd"] = "desc" 
    return Search(**self._parameters)

  def ascending(self):
    self._parameters["sd"] = "asc"
    return Search(**self._parameters)

  def sort_by(self, sf):
    self._parameters["sf"] = sf
    return Search(**self._parameters)


if version_info < (3, 0):
  def next(self):
    return self._search.next()

  Search.next = next

else:
  def __next__(self):
    return next(self._search)

  Search.__next__ = __next__

