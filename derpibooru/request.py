
from requests import get, codes 
from .search import search_random

def search_random_request(hostname, q, key):
  url = search_random(hostname, q, key)

  request = get(url)

  if request.status_code == codes.ok:
    index = request.json()["id"]
    return index
