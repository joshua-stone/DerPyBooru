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

