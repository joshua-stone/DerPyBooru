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

  @q.setter
  def q(self, q=[]):
    self.__q = q

  @property
  def page(self):
    return(self.__page)

  @page.setter
  def page(self, page=1):
    self.__page = page

  @property
  def comments(self):
    return(self.__comments)

  @comments.setter
  def comments(self, comments=True):
    self.__comments = comments

  @property
  def key(self):
    return(self.__key)

  @key.setter
  def key(self, key=""):
    self.__key = key

  @property
  def fav(self):
    return(self.__fav)

  @fav.setter
  def fav(self, fav=True):
    self.__fav = fav

