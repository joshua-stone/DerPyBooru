class Search(object):
  def __init__(self, q=[], page=1, comments=False, fav=False, key=""):
    self.q = q
    self.page = page
    self.comments = comments
    self.fav = fav
    self.key = key

  @property
  def hostname(self):
    return("https://derpiboo.ru")

  @property
  def q(self):
    return(self.__q)

  @property
  def page(self):
    return(self.__page)

  @property
  def comments(self):
    return(self.__comments)

