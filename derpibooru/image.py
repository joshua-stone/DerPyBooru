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

class Image(object):
  """
  This class provides a thin wrapper around JSON data, mapping each value to
  its own property. Once instantiated the data is immutable so as to reflect
  the stateless nature of a REST API
  """
  def __init__(self, data):
    self.__data = data

  @property
  def id(self):
    return(self.data["id"])

  @property
  def tags(self):
    return(self.data["tags"].split(", "))

  @property
  def is_optimized(self):
    return(self.data["is_optimized"])

  @property
  def sha512_hash(self):
    return(self.data["sha512_hash"])

  @property
  def upvotes(self):
    return(self.data["upvotes"])

  @property
  def aspect_ratio(self):
    return(self.data["aspect_ratio"])

  @property
  def original_format(self):
    return(self.data["original_format"])

  @property
  def mime_type(self):
    return(self.data["mime_type"])

  @property
  def height(self):
    return(self.data["height"])

  @property
  def updated_at(self):
    return(self.data["updated_at"])

  @property
  def width(self):
    return(self.data["width"])

  @property
  def comment_count(self):
    return(self.data["comment_count"])

  @property
  def tag_ids(self):
    return(self.data["tag_ids"])

  @property
  def created_at(self):
    return(self.data["created_at"])

  @property
  def file_name(self):
    return(self.data["file_name"])

  @property
  def uploader(self):
    return(self.data["uploader"])

  @property
  def description(self):
    return(self.data["description"])

  @property
  def orig_sha512_hash(self):
    return(self.data["orig_sha512_hash"])

  @property
  def id_number(self):
    return(self.data["id_number"])

  @property
  def license(self):
    return(self.data["license"])

  @property
  def thumb(self):
    return("https:" + self.data["representations"]["thumb"])

  @property
  def thumb_tiny(self):
    return("https:" + self.data["representations"]["thumb_tiny"])

  @property
  def small(self):
    return("https:" + self.data["representations"]["small"])

  @property
  def full(self):
    return("https:" + self.data["representations"]["full"])

  @property
  def tall(self):
    return("https:" + self.data["representations"]["tall"])

  @property
  def large(self):
    return("https:" + self.data["representations"]["large"])

  @property
  def medium(self):
    return("https:" + self.data["representations"]["medium"])

  @property
  def thumb_small(self):
    return("https:" + self.data["representations"]["thumb_small"])

  @property
  def image(self):
    return("https:" + self.data["image"])

  @property
  def score(self):
    return(self.data["score"])

  @property
  def downvotes(self):
    return(self.data["downvotes"])

  @property
  def duplicate_reports(self):
    return(self.data["duplicate_reports"])

  @property
  def faves(self):
    return(self.data["faves"])

  @property
  def source_url(self):
    return(self.data["source_url"])

  @property
  def is_rendered(self):
    return(self.data["is_rendered"])

  @property
  def data(self):
    return(self.__data)

