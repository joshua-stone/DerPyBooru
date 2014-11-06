from .search import search, search_random
from .watched import watched, watched_random, watched_user, watched_user_random

class Derpibooru(object):
  def __init__(self, q=[], key="", user_id="", perpage=15, comments=False, fav=False):
    self._parameters = {}
    self.q = q
    self.key = key
    self.user_id = user_id
    self.perpage = perpage
    self.comments = comments
    self.fav = fav

  @property
  def hostname(self):
    return("https://derpiboo.ru")

  @property
  def q(self):
    return(self._parameters["q"])

  @q.setter
  def q(self, q=[]):
    if not isinstance(q, list):
      raise TypeError("tags must be a list of strings")

    for tag in q:
      if not isinstance(tag, str):
        raise TypeError("{0} is not a string".format(tag))

      if "," in tag or tag == "":
        raise ValueError("tags can't contain commas or be empty strings")

    self._parameters["q"] = [tag.strip() for tag in q]

  @property
  def key(self):
    return(self.parameters["key"])

  @key.setter
  def key(self, key=""):
    if not isinstance(key, str):
      raise TypeError("key must be a string")

    self._parameters["key"] = key

  @property
  def user_id(self):
    return(self.parameters["user_id"])

  @user_id.setter
  def user_id(self, user_id=""):
    if not isinstance(user_id, str):
      raise TypeError("user ID must be a string")

    self._parameters["user_id"] = user_id

  @property
  def perpage(self):
    return(self.parameters["perpage"])

  @perpage.setter
  def perpage(self, page_size):
    if not isinstance(page_size, int):
      raise TypeError("perpage must be an int")
    if page_size not in range(1, 51):
      raise ValueError("perpage must be within range of 1-50")

    self._parameters["perpage"] = page_size

  @property
  def comments(self):
    return(self.parameters["comments"])

  @comments.setter
  def comments(self, comments=True):
    if not isinstance(comments, bool):
      raise TypeError("comments must be either True or False")

    self._parameters["comments"] = comments

  @property
  def fav(self):
    return(self.parameters["fav"])

  @fav.setter
  def fav(self, fav=True):
    if not isinstance(fav, bool):
      raise TypeError("favorites must be either True or False")

    self._parameters["fav"] = fav

  @property
  def parameters(self):
    return(self._parameters)

  def search(self):
    url = search(self.hostname, self.q, 1, self.perpage, self.comments, self.fav)

    return(url)

  def search_random(self):
    url = search_random(self.hostname, self.q)

    return(url)

  def watched(self):
    url = watched(self.hostname, self.key, self.perpage, 1, self.comments, self.fav)

    return(url)

  def watched_random(self):
    url = watched_random(self.hostname, self.key)

    return(url)

  def watched_user(self):
    url = watched_user(self.hostname, self.user_id, self.perpage, 1, self.comments, self.fav)

    return(url)

  def watched_user_random(self):
    url = watched_user_random(self.hostname, self.user_id)

    return(url) 
