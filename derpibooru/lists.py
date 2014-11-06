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

from .parameters import Parameters

class Top_Scoring(Parameters):

  def __init__(self, last=(0,"h"), page=1, perpage=15, comments=False, fav=False, key=""):
    super(Top_Scoring, self).__init__(key, page, perpage, comments, fav)
    self.last = last

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
  def url(self):
    parameters = []

    parameters.append("page={0}".format(self.page))

    if self.last[0] > 0:
      parameters.append("last={0}{1}".format(self.last[0], self.last[1]))

    if self.fav == True:
      parameters.append("fav=")

    if self.comments == True:
      parameters.append("comments=")

    url = (self.hostname + "/lists/top_scoring.json")

    if parameters != []:
      url += ("?" + "&".join(parameters))

    return(url)

class All_Time_Top_Scoring(Parameters):

  def __init__(self, last=(0,"h"), page=1, perpage=15, comments=False, fav=False, key=""):
    super(All_Time_Top_Scoring, self).__init__(key, page, perpage, comments, fav)
    self.last = last

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
  def url(self):
    parameters = []

    parameters.append("page={0}".format(self.page))

    if self.last[0] > 0:
      parameters.append("last={0}{1}".format(self.last[0], self.last[1]))

    if self.fav == True:
      parameters.append("fav=")

    if self.comments == True:
      parameters.append("comments=")

    url = (self.hostname + "/lists/all_time_top_scoring.json")

    if parameters != []:
      url += ("?" + "&".join(parameters))

    return(url)

class Top_Commented(Parameters):

  def __init__(self, last=(0,"h"), page=1, perpage=15, comments=False, fav=False, key=""):
    super(Top_Commented, self).__init__(key, page, perpage, comments, fav)
    self.last = last

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
  def url(self):
    parameters = []

    parameters.append("page={0}".format(self.page))

    if self.last[0] > 0:
      parameters.append("last={0}{1}".format(self.last[0], self.last[1]))

    if self.fav == True:
      parameters.append("fav=")

    if self.comments == True:
      parameters.append("comments=")

    url = (self.hostname + "/lists/top_commented.json")

    if parameters != []:
      url += ("?" + "&".join(parameters))

    return(url)

