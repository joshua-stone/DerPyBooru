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
from .image import Image

__all__ = [
  "tags",
  "api_key",
  "url",
  "request",
  "get_image_data"
]

if version_info < (3, 0):
  from urllib import urlencode
else:
  from urllib.parse import urlencode

def tags(q):
  tags = {str(tag).strip() for tag in q if tag}

  return tags if tags else {}

def api_key(api_key):
  return str(api_key) if api_key else ""

def format_params(params):
  p = {}

  for key, value in params.items():
    if key == "key":
      if value:
        p["key"] = value
    elif key == "q":
      p["q"] = ",".join(value) if value else "*"
    else:
      p[key] = value

  return p

def url(params):
  p = format_params(params)
  url = "https://derpiboo.ru/search?{}".format(urlencode(p))

  return url

def request(params):
  search = "https://derpiboo.ru/search.json"

  request = get(search, params=params)

  while request.status_code == codes.ok:
    images, image_count = request.json()["search"], 0
    for image in images:
      yield Image(image)
      image_count += 1
    if image_count < 50:
      break

    p["page"] += 1
    request = get(search, params=params)

def get_images(key="", q={}, sf="created_at", sd="desc", limit=50):
  params = format_params({
    "key": key,
    "q":  q,
    "sf": sf,
    "sd": sd,
    "page": 1,
    "perpage": 50
  })
  
  if limit is not None:
    l = int(limit)
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
  url = "https://derpiboo.ru/{}.json?fav=&comments=".format(id_number)

  request = get(url)

  if request.status_code == codes.ok:
    data = request.json()

    return data

