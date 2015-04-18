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

from requests import get, codes
from sys import version_info
from .helpers import format_params, join_params

__all__ = [
  "url",
  "request",
  "get_images",
  "get_image_data",
  "set_limit"
]

if version_info < (3, 0):
  from urllib import urlencode
else:
  from urllib.parse import urlencode

def url(params):
  p = format_params(params)
  url = "https://derpibooru.org/search?{}".format(urlencode(p))

  return url

def request(params):
  search, p = "https://derpibooru.org/search.json", format_params(params)

  request = get(search, params=p)

  while request.status_code == codes.ok:
    images, image_count = request.json()["search"], 0
    for image in images:
      yield image
      image_count += 1
    if image_count < 50:
      break

    p["page"] += 1

    request = get(search, params=p)

def get_images(parameters, limit=50):
  params = join_params(parameters, {"perpage": 50, "page": 1})

  if limit is not None:
    l = limit
    if l > 0:
      r, counter = request(params), 0
      for index, image in enumerate(r, start=1):
        yield image
        if index >= l:
          break
  else:
    r = request(params)
    for image in r:
      yield image

def get_image_data(id_number):
  url = "https://derpibooru.org/{}.json?fav=&comments=".format(id_number)

  request = get(url)

  if request.status_code == codes.ok:
    data = request.json()

    if "duplicate_of" in data:
      return get_image_data(data["duplicate_of"])
    else:
      return data

