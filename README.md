# DerPyBooru

Python bindings for Derpibooru's API

License: **Simplified BSD License**

Version: **0.7**

## Features

- High-level abstraction over Derpibooru's REST API
- Parameter chaining for ease of manipulation
- Syntactic sugar for queries, e.g., "query.score >= 100" compiling to "score.gte:100"
- Design focusing on iterables and lazy generation for network efficiency

## Dependencies

- python2.7 or newer
- requests

## How to install

### Python 2.7

    $ pip install derpybooru

### Python 3.x

    $ pip3 install derpybooru
 
## Checking documentation

### Python 2.7

    $ pydoc derpibooru

### Python 3.x

    $ pydoc3 derpibooru

## Typical usage

### Getting images currently on Derpibooru's front page

```python
from derpibooru import Search

for image in Search():
  id_number, score, tags = image.id_number, image.score, ", ".join(image.tags)
  print("#{} - score: {:>3} - {}".format(id_number, score, tags))
```

### Searching posts by tag

```python
from derpibooru import Search

for image in Search().query("rarity", "twilight sparkle"):
  print(image.url)
```

### Crawling Derpibooru from first to last post

```python
from derpibooru import Search

# This is only an example and shouldn't be used in practice as it abuses
# Derpibooru's licensing terms
for image in Search().ascending().limit(None):
  id_number, score, tags = image.id_number, image.score, ", ".join(image.tags)
  print("#{} - score: {:>3} - {}".format(id_number, score, tags))
```

### Getting random posts

```python
from derpibooru import Search, sort

for post in Search().sort_by(sort.RANDOM):
  print(post.url)
```

### Getting top 100 posts
```python
from derpibooru import Search, sort

top_scoring = [post for post in Search().sort_by(sort.SCORE).limit(100)]
```

### Storing and passing new search parameters

```python
from derpibooru import Search, sort

params = Search().sort_by(sort.SCORE).limit(100).parameters

top_scoring = Search(**params)
top_animated = top_scoring.query("animated")
```

### Filtering by metadata

```python
from derpibooru import Search, query

q = {
  "wallpaper",
  query.width == 1920,
  query.height == 1080,
  query.score >= 100
}

wallpapers = [image for image in Search().query(*q)]
```
### Getting the latest images from a watchlist

```python

from derpibooru import Search, user

key = "your_api_key"

for post in Search().key(key).watched(user.ONLY):
  id_number, score, tags = post.id_number, post.score, ", ".join(post.tags)
  print("#{} - score: {:>3} - {}".format(id_number, score, tags))

