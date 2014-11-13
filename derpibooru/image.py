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

from re import sub
from .request import get_image_data
from .comment import Comment

__all__ = [
  "Image"
]

class Image(object):
  """
  This class provides a thin wrapper around JSON data, mapping each value to
  its own property. Once instantiated the data is immutable so as to reflect
  the stateless nature of a REST API
  """
  def __init__(self, data):
    self._data = data
    for field in data:
      if not hasattr(self, field):
        setattr(self, field, self.data[field]) 

  def __str__(self):
    return "Image({0})".format(self.id_number)

  @property
  def tags(self):
    return self.data["tags"].split(", ")
  def thumb(self):
    return "https:" + self.data["representations"]["thumb"]

  @property
  def thumb_tiny(self):
    return "https:" + self.data["representations"]["thumb_tiny"]

  @property
  def small(self):
    return "https:" + self.data["representations"]["small"]

  @property
  def full(self):
    return "https:" + self.data["representations"]["full"]

  @property
  def tall(self):
    return "https:" + self.data["representations"]["tall"]

  @property
  def large(self):
    return "https:" + self.data["representations"]["large"]

  @property
  def medium(self):
    return "https:" + self.data["representations"]["medium"]

  @property
  def thumb_small(self):
    return "https:" + self.data["representations"]["thumb_small"]

  @property
  def image(self):
    return "https:" + self.data["image"]

  @property
  def image_shortened(self):
    url = sub("_.*\.", ".", self.image)

    return url

  @property
  def faved_by(self):
    faved_by = "favourited_by_users"

    if not faved_by in self.data:
      if self.faves > 0:
        self.update()
      else:
        self._data[faved_by] = []

    return self._data[faved_by]

  @property
  def comments(self):
    if not "comments" in self.data:
      if self.comment_count > 0:
        self.update()
      else:
        self._data["comments"] = []

    return [Comment(c) for c in self.data["comments"]]
       
  @property
  def url(self):
    return "https://derpiboo.ru/{}".format(self.id_number)

  @property
  def data(self):
    return self._data

  def update(self):
    data = get_image_data(self.id_number)

    if data:
      self._data = data

