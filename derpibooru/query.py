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

__all__ = [
  "query"
]
 
class Equal(object):
  def __init__(self, name):
    self.name = name

  def __eq__(self, value):
    if value:
      return "{}:{}".format(self.name, value)
    else:
      raise ValueError(value)

  def __gt__(self, value):
    raise AttributeError("gt")

  def __lt__(self, value):
    raise AttributeError("lt")

  def __ge__(self, value):
    raise AttributeError("ge")

  def __le__(self, value):
    raise AttributeError("le")
 
 
class Comparable(object):
  def __init__(self, name):
    self.name = name

  def op(self, op, value):
    try:
      float(value)
      return "{}.{}:{}".format(self.name, op, value)
    except:
      raise ValueError(value)

  def __eq__(self, value):
    return self.op("eq", value)

  def __gt__(self, value):
    return self.op("gt", value)

  def __lt__(self, value):
    return self.op("lt", value)

  def __ge__(self, value):
    return self.op("gte", value)

  def __le__(self, value):
    return self.op("lte", value)

    
class Query(object):
  def __init__(self):
    for field in ["description", "faved_by", "source_url", "orig_sha512_hash",
                  "source_url", "sha512_hash", "uploader"]:
      setattr(self, field, Equal(field))

    for field in ["aspect_ratio", "downvotes", "faves", "height", "score",
                  "upvotes", "width"]:
      setattr(self, field, Comparable(field))

  def __neg__(self):
    return self.__class__()

query = Query()
