
__all__ = [
  "tags",
  "api_key",
  "sort_format",
  "format_params"
]

from .sort import sorting_methods

def tags(q):
  tags = {str(tag).strip() for tag in q if tag}

  return tags if tags else {}

def api_key(api_key):
  return str(api_key) if api_key else ""

def sort_format(sf):
  if sf not in sorting_methods:
    raise ValueError("`{}' is not a valid sorting method".format(sf))

  return sf

def format_params(params):
  p = {}

  for key, value in params.items():
    if key == "key":
      if value:
        p["key"] = value
    elif key == "q":
      p["q"] = ",".join(value) if value else "*"
    else:
      p[key] = value

  return p

