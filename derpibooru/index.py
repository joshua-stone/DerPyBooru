
class Index(object):
  def__init__(self, id_number, comments=False, fav=False):
    self.parameters = {}
    self.id_number = id_number
    self.comments = False
    self.fav = False
  def

  @property
  def hostname(self):
    return("https://derpiboo.ru")

  @property
  def id_number(self):
    return(self.parameters["id_number"])

  @id_number.setter
  def id_number(self, id_number):
    if not isinstance(comments, int):
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

