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
  "tags",
  "api_key",
  "sort_format",
  "format_params",
  "join_params"
]

from .sort import sort
from .user import user

def tags(q):
  tags = {str(tag).strip() for tag in q if tag}

  return tags if tags else {}

def api_key(api_key):
  return str(api_key) if api_key else ""

def validate_filter(filter_id):
  # is it always an number?
  return str(filter_id) if filter_id else ""

def sort_format(sf):
  if sf not in sort.methods:
    raise AttributeError(sf)
  else:
    return sf

def user_option(option):
  if option: 
    if option not in user.options:
      raise AttributeError(option)
    else:
      return option
  else:
    return ""

def format_params(params):
  p = {}

  for key, value in params.items():
    if key == "key":
      if value:
        p["key"] = value
    elif key in ("faves", "upvotes", "uploads", "watched"):
      if value and params["key"]:
        p[key] = value
    elif key == "q":
      p["q"] = ",".join(value) if value else "*"
    else:
      p[key] = value

  return p

def join_params(old_params, new_params):
  new_dict = dict(list(old_params.items()) + list(new_params.items()))

  return new_dict

def set_limit(limit):

  if limit is not None:
    l = int(limit)
  else:
    l = None

  return l

