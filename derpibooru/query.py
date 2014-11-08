def Derpibooru(key=(), q=[], comments=False, fav=False, perpage=50,
               random=False, last=(0,"h")):
  parameters = {
    "key": key,
    "q": q,
    "comments": comments,
    "fav": fav,
    "perpage": perpage, 
    "random": random,
    "last": last
  }
  return Query(parameters)

class Query(object):
  def __init__(self, data={}):
    self._parameters = data

  @property
  def parameters(self):
    return self._parameters

  def api_key(self, key=""):
    self.parameters["key"] = ("api_key", key)
    return Query(self.parameters)

  def user_id(self, user_id=""):
    self.parameters["key"] = ("user_id", key)
    return Query(self.parameters)

  def q(self, q=[]):
    self.parameters["q"] = [str(tag).strip() for tag in q]
    return Query(self.parameters)

  def comments(self, comments=False):
    self.parameters["comments"] = comments
    return Query(self.parameters)

  def fav(self, fav=False):
    self.parameters["fav"] = fav
    return Query(self.parameters)

  def perpage(self, perpage=50):
    self.parameters["perpage"] = perpage
    return Query(self.parameters)

  def random(self, random=True):
    self.parameters["random"] = random
    return Query(self.parameters)

  def last(self, last=(0,"h")):
    self.parameters["last"] = last
    return Query(self.parameters)

