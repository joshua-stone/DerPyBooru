class Search(object):
  def __init__(self, key={}, q=[], sf="created_at", sd="desc"):
    self._parameters = {
      "key": key,
      "q": q,
      "sf": sf,
      "sd": sd
    }

  @property
  def parameters(self):
    return self._parameters

  def api_key(self, key=""):
    self._parameters["key"] = {"api_key": key}
    return Search(**self._parameters)

  def user_id(self, user_id=""):
    self._parameters["key"] = {"user_id": key}
    return Search(**self._parameters)

  def q(self, q):
    self._parameters["q"] = [str(tag).strip() for tag in q]
    return Search(**self._parameters)

  def descending(self):
    self._parameters["sd"] = "desc" 
    return Search(**self._parameters)

  def ascending(self):
    self._parameters["sd"] = "asc"
    return Search(**self._parameters)

