
class Lists(object):

  def __init__(self, list_index=0, page=1, last=(0,"h"), comments=False, fav=False, key=""):
    self.__parameters = {}
    self.list = list_index
    self.page = page
    self.last = last
    self.comments = comments
    self.fav = fav
    self.key = key

  @property
  def hostname(self):
    return("https://derpiboo.ru")

  @property
  def parameters(self):
    return(self.__parameters)

  @property
  def available_lists(self):
    lists = {
      0: "index",
      1: "top_scoring",
      2: "all_time_top_scoring",
      3: "top_commented"
    }

    return(lists)

  @property
  def list(self):
    return(self.parameters["list"])

  @list.setter
  def list(self, list_index=0):
    if not isinstance(list_index, int):
      raise TypeError("list value must be an int")
    if 0 > list_index > 3:
      raise ValueError("list index needs to be between 0 and 3")
    self.__parameters["list"] = list_index

  @property
  def page(self):
    return(self.parameters["page"])

  @page.setter
  def page(self, page=1):
    if not isinstance(page, int):
      raise TypeError("page number must be an int")

    if page < 1:
      raise ValueError("page number must be greater than 1")

    self.__parameters["page"] = page

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

    self.__parameters["last"] = time

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
  def key(self):
    return(self.parameters["key"])

  @key.setter
  def key(self, key=""):
    if not isinstance(key, str):
      raise TypeError("key must be a string")

    self.__parameters["key"] = key

  @property
  def url(self):

    lists, parameters = self.available_lists[self.list], []

    if self.list != 0:
      parameters.append("page={0}".format(self.page))

    if self.last[0] > 0:
      parameters.append("last={0}{1}".format(self.last[0], self.last[1]))

    if self.fav == True:
      parameters.append("fav=")

    if self.comments == True:
      parameters.append("comments=")

    url = (self.hostname + "/lists/" + lists + ".json")

    if parameters != []:
      url += ("?" + "&".join(parameters))

    return(url)

