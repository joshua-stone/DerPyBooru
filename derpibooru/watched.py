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

def watched(hostname, key, perpage, page, comments, fav):
  url = watched_url(hostname, "key", key, perpage, page, comments, fav)

  return(url)

def watched_random(hostname, key):
  url = watched_random_url(hostname, "key", key)

  return(url)

def watched_user(hostname, user_id, perpage, page, comments, fav):
  url = watched_url(hostname, "user_id", user_id, perpage, page, comments, fav)

  return(url)

def watched_user_random(hostname, user_id):
  url = watched_random_url(hostname, "user_id", user_id)

  return(url)

def watched_url(hostname, key, value, perpage, page, comments, fav):
  url, parameters = hostname + "/images/watched.json", []

  parameters.append("{0}={1}".format(key, value))
  parameters.append("perpage={0}".format(perpage))
  parameters.append("page={0}".format(page))

  if comments == True:
    parameters.append("comments=")
  if fav == True:
    parameters.append("fav=")

  url += "?{0}".format("&".join(parameters))

  return(url)

def watched_random_url(hostname, key, value):
  url = "{0}/images/watched.json?random=y&{1}={2}".format(hostname, key, value)

  return(url)
