from .request import url

class Search(object):
  def __init__(self, key=None, q=[], sf="created_at", sd="desc"):
    self._parameters = {
      "key": key,
      "q": q,
      "sf": sf,
      "sd": sd
    }

  @property
  def parameters(self):
    return self._parameters

  @property
  def url(self):
    return url(**self.parameters)

  def key(self, key=None):
    self._parameters["key"] = key
    return Search(**self._parameters)

  def query(self, *q):
    self._parameters["q"] = [str(tag).strip() for tag in q]
    return Search(**self._parameters)

  def descending(self):
    self._parameters["sd"] = "desc" 
    return Search(**self._parameters)

  def ascending(self):
    self._parameters["sd"] = "asc"
    return Search(**self._parameters)

  def sort_by(self, sf):
    self._parameters["sf"] = sf
    return Search(**self._parameters)

