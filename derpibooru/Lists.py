
class Lists(object)

  def __init__(self, page=1, last="", comments=False, fav=False, key=""):
    self.__parameters = {}

  @property
  def hostname()
    return("https://derpiboo.ru")

  @property
  def parameters(self):
    return(self.__parameters)

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

