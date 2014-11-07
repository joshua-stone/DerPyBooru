def images(hostname, lists, key, value, perpage, page, comments, fav):
  url, parameters = "{0}/images/{1}.json".format(hostname, lists), []

  parameters.append("{0}={1}".format(key, value))
  parameters.append("perpage={0}".format(perpage))
  parameters.append("page={0}".format(page))

  if comments == True:
    parameters.append("comments=")
  if fav == True:
    parameters.append("fav=")

  url += "?{0}".format("&".join(parameters))

  return(url)

def images_random(hostname, lists, key, value):
  url = "{0}/images/{1}.json?random=y&{2}={3}".format(hostname, lists, key, value)

  return(url)


def lists(hostname, lists, perpage, page, duration, unit):
  url, parameters = "{0}/lists/{1}.json".format(hostname, lists), []

  parameters.append("page={0}".format(page))
  parameters.append("perpage={0}".format(perpage))

  if duration > 0:
    parameters.append("last={0}{1}".format(duration, unit))

  url += ("?" + "&".join(parameters))

  return(url)

def lists_random(hostname, lists, key):
  url = "{0}/lists/{1}.json?random=y&{2}".format(hostname, lists, key)

  return(url)

