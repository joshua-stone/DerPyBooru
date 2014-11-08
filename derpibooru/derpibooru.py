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

from .search import search, search_random
from .watched import watched, watched_random, watched_user, watched_user_random
from .faves import faves, faves_random, faves_user, faves_user_random
from .uploaded import uploaded, uploaded_random, uploaded_user, uploaded_user_random
from .lists import top_scoring, all_time_top_scoring, top_commented
from .request import search_random_request
class Derpibooru(object):
  def __init__(self, q=[], key="", user_id="", perpage=15, comments=False, fav=False, last=(0,"h")):
    self._parameters = {}
    self.q = q
    self.key = key
    self.user_id = user_id
    self.perpage = perpage
    self.comments = comments
    self.fav = fav
    self.last = last

  @property
  def hostname(self):
    return("https://derpiboo.ru")

  @property
  def q(self):
    return(self._parameters["q"])

  @q.setter
  def q(self, q=[]):
    if not isinstance(q, list):
      raise TypeError("tags must be a list of strings")

    for tag in q:
      if not isinstance(tag, str):
        raise TypeError("{0} is not a string".format(tag))

      if "," in tag or tag == "":
        raise ValueError("tags can't contain commas or be empty strings")

    self._parameters["q"] = [tag.strip() for tag in q]

  @property
  def key(self):
    return(self.parameters["key"])

  @key.setter
  def key(self, key=""):
    if not isinstance(key, str):
      raise TypeError("key must be a string")

    self._parameters["key"] = key

  @property
  def user_id(self):
    return(self.parameters["user_id"])

  @user_id.setter
  def user_id(self, user_id=""):
    if not isinstance(user_id, str):
      raise TypeError("user ID must be a string")

    self._parameters["user_id"] = user_id

  @property
  def perpage(self):
    return(self.parameters["perpage"])

  @perpage.setter
  def perpage(self, page_size):
    if not isinstance(page_size, int):
      raise TypeError("perpage must be an int")
    if page_size not in range(1, 51):
      raise ValueError("perpage must be within range of 1-50")

    self._parameters["perpage"] = page_size

  @property
  def comments(self):
    return(self.parameters["comments"])

  @comments.setter
  def comments(self, comments=True):
    if not isinstance(comments, bool):
      raise TypeError("comments must be either True or False")

    self._parameters["comments"] = comments

  @property
  def fav(self):
    return(self.parameters["fav"])

  @fav.setter
  def fav(self, fav=True):
    if not isinstance(fav, bool):
      raise TypeError("favorites must be either True or False")

    self._parameters["fav"] = fav

  @property
  def last(self):
    return(self.parameters["last"])

  @last.setter
  def last(self, time=(0,"")):
    if not isinstance(time[0], int):
      raise TypeError("sampling period duration must be an integer")
    if not time[0] >= 0:
      raise ValueError("sampling period duration must be positive")
    if not isinstance(time[1], str):
      raise TypeError("sampling period unit must be string")
    if not time[1] in ("h", "d", "w"):
      raise ValueError("sampling period unit must be `h', `d', or `w'")

    self._parameters["last"] = time

  @property
  def parameters(self):
    return(self._parameters)

  def search(self):
    url = search(self.hostname, self.q, 1, self.perpage, self.comments, self.fav)

    return(url)

  def search_random(self):
    index = search_random_request(self.hostname, self.q, self.key)

    return index

  def watched(self):
    url = watched(self.hostname, self.key, self.perpage, 1, self.comments, self.fav)

    return(url)

  def watched_random(self):
    url = watched_random(self.hostname, self.key)

    return(url)

  def watched_user(self):
    url = watched_user(self.hostname, self.user_id, self.perpage, 1, self.comments, self.fav)

    return(url)

  def watched_user_random(self):
    url = watched_user_random(self.hostname, self.user_id)

    return(url)

  def faves(self):
    url = faves(self.hostname, self.key, self.perpage, 1, self.comments, self.fav)

    return(url)

  def faves_random(self):
    url = faves_random(self.hostname, self.key)

    return(url)

  def faves_user(self):
    url = faves_user(self.hostname, self.user_id, self.perpage, 1, self.comments, self.fav)

    return(url)

  def faves_user_random(self):
    url = faves_user_random(self.hostname, self.user_id)

    return(url)


  def uploaded(self):
    url = uploaded(self.hostname, self.key, self.perpage, 1, self.comments, self.fav)

    return(url)

  def uploaded_random(self):
    url = uploaded_random(self.hostname, self.key)

    return(url)

  def uploaded_user(self):
    url = uploaded_user(self.hostname, self.user_id, self.perpage, 1, self.comments, self.fav)

    return(url)

  def uploaded_user_random(self):
    url = uploaded_user_random(self.hostname, self.user_id)

    return(url)

  def top_scoring(self):
    url = top_scoring(self.hostname, self.key, 1, self.perpage, self.last[0], self.last[1])

    return(url)

  def all_time_top_scoring(self):
    url = all_time_top_scoring(self.hostname, self.key, 1, self.perpage, self.last[0], self.last[1])

    return(url)


  def top_commented(self):
    url = top_commented(self.hostname, self.key, 1, self.perpage, self.last[0], self.last[1])

    return(url)

