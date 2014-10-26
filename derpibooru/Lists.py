
class Lists(object)

  def __init__(self, lists, page=1, last="", comments=False, fav=False, key=""):
    self.__parameters = {}

  @property
  def hostname()
    return("https://derpiboo.ru")

  @property
  def parameters(self):
    return(self.__parameters)

  @property
  def lists():
    lists = {
      0: "index",
      1: "scoring_scoring",
      2: "all_time_top_scoring",
      3: "top_commented"
    }

    return(lists)

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

