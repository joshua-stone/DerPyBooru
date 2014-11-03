
class Watched(object):
  def __init__(self, key, page=1, perpage=15, comments=False, fav=False):
    self.__parameters = {}
    self.key = key
    self.page = page
    self.perpage = perpage
    self.comments = comments
    self.fav = fav

  @property
  def hostname(self):
    return("https://derpiboo.ru")

  @property
  def key(self):
    return(self.parameters["key"])

  @key.setter
  def key(self, key=""):
    if not isinstance(key, str):
      raise TypeError("key must be a string")

    self.__parameters["key"] = key

  @property
  def page(self):
    return(self.parameters["page"])

  @page.setter
  def page(self, page=1):
    if not isinstance(page, int):
      raise TypeError("page number must be an int")

    if page < 1:
      raise ValueError("page number must be greater than 0")

    self.__parameters["page"] = page

  def next_page(self, number=1):
    if not isinstance(number, int):
      raise TypeError("page number must be an int")

    if number < 1:
      raise ValueError("page number must be greater than 0")

    self.__parameters["page"] += number

  def previous_page(self, number=1):
    if not isinstance(number, int):
      raise TypeError("page number must be an int")

    if number < 1:
      raise ValueError("page number must be greater than 0")

    if self.parameters["page"] - number <= 1:
      self.__parameters["page"] = 1
    else:
      self.__parameters["page"] -= number

  @property
  def perpage(self):
    return(self.parameters["perpage"])

  @perpage.setter
  def perpage(self, page_size):
    if not isinstance(page_size, int):
      raise TypeError("perpage must be an int")
    if page_size not in range(1, 51):
      raise ValueError("perpage must be within range of 1-50")

    self.__parameters["perpage"] = page_size

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
    url, parameters = self.hostname + "images/watched.json", []
    
    parameters.append("key={0}".format(self.key))
    parameters.append("perpage={0}".format(self.perpage))
    parameters.append("page={0}".format(self.page))

    if self.comments == True:
      parameters.append("comments=")
    if self.fav == True:
      parameters.append("fav=")

    url += "?{0}".format("&".join(parameters))

    return(url)
