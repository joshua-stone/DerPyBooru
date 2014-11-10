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

if version_info < (3, 0):
  from urllib import quote_plus
else:
  from urllib.parse import quote_plus


def join_tags(tags):
  q = quote_plus(",".join(tags))

  return q

def join_parameters(parameters):
  p = ["{}={}".format(k, v) for k, v in parameters.items()]

  return p

def url(parameters):
  url, p = "https://derpiboo.ru/search.json?", {}

  for key, value in parameters.items():
    if key == "key":
      if value:
        p["key"] = value
    elif key == "q":
      p["q"] = join_tags(value) if value else "*"
    else:
      p[key] = value
  
  url += "&".join(join_parameters(p))

  return url

def request(parameters):
  p = parameters
  p.update({ "page": 1, "perpage": 50})

  request = get(url(p))

  while request.status_code == codes.ok:
    for image in request.json()["search"]:
      yield Image(image)

    parameters["page"] += 1

    request = get(url(p))

  yield None
