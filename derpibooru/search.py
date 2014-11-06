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

def search(hostname, q, page, perpage, comments, fav):
  url, parameters = hostname, []

  if q == []:
    search = "/images/page/{0}.json".format(page)
  else:
    search, tags = "/search.json", ",".join(q)
    parameters.append("q={0}".format(tags.replace(" ", "+")))
    parameters.append("page={0}".format(page))

  if comments == True:
    parameters.append("comments=")

  if fav == True:
    parameters.append("fav=")

  parameters.append("perpage={0}".format(perpage))

  url += search

  if parameters != []:
    url += "?{0}".format("&".join(parameters))

  return(url)

def search_random(hostname, q):
  url = hostname

  if q == []:
    url += "/images/random.json"
  else:
    url += "/search.json?random_image=y"

    tags = ",".join(q)

    url += "&q={0}".format(tags.replace(" ", "+"))

  return(url)

