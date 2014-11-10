
from requests import get, codes

def join_tags(tags):
  q = ",".join(tags)

  return q

def join_parameters(parameters):
  p = ["{}={}".format(k, v) for k, v in parameters.items()]

  return p

def url(key=(), q=[], sf="created_at", sd="desc"):
  url, parameters = "https://derpiboo.ru/search.json?", {}

  if key:
    parameters[key[0]] = key[1]

  parameters["q"] = join_tags(q) if q else "*"

  parameters["sf"] = sf
  parameters["sd"] = sd

  url += "&".join(join_parameters(parameters))

  return url

#def search(parameters):
#  url = search_random(hostname, q, key)
#
#  request = get(url)
#
#  if request.status_code == codes.ok:
#    index = request.json()["id"]
#    return index
