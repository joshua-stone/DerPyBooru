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

class Index(object):
  def __init__(self, id_number, comments=False, fav=False):
    self.__parameters = {}
    self.id_number = id_number
    self.comments = comments
    self.fav = fav

  @property
  def hostname(self):
    return("https://derpiboo.ru")

  @property
  def id_number(self):
    return(self.parameters["id_number"])

  @id_number.setter
  def id_number(self, id_number):
    if not isinstance(id_number, int):
      raise TypeError("image ID number must be either a positive int")
    if id_number < 1:
      raise ValueError("image ID number can't be less than 1")

    self.__parameters["id_number"] = id_number

  @property
  def comments(self):
    return(self.parameters["comments"])

  @comments.setter
  def comments(self, comments=True):
    if not isinstance(comments, bool):
      raise TypeError("comments must be either True or False")

    self.__parameters["comments"] = comments

  @property
  def fav(self):
    return(self.parameters["fav"])

  @fav.setter
  def fav(self, fav=True):
    if not isinstance(fav, bool):
      raise TypeError("favorites must be either True or False")

    self.__parameters["fav"] = fav

  @property
  def parameters(self):
    return(self.__parameters)

  @property
  def url(self):
    url, parameters = "{0}/{1}.json".format(self.hostname, self.id_number), []

    if self.comments == True:
      parameters.append("comments=")

    if self.fav == True:
      parameters.append("fav=")

    if parameters != []:
     url += "?{0}".format("&".join(parameters))

    return(url)

   

