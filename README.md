# DerPyBooru

Python bindings for Derpibooru's API

License: **Simplified BSD License**

## Dependencies

- python2.7 or newer
- requests

## How to install

    pip install https://github.com/joshua-stone/pyderpibooru/zipball/master

##Typical usage

###Getting images currently on Derpibooru's front page

```python
from derpibooru import Search

for image in Search():
  id, score, tags = image.id_number, image.score, ", ".join(image.tags)
  print("#{} - score: {:>2} - {}".format(id, score, tags))
```

###Searching by tag

```python
from derpibooru import Search

for image in Search().query("rarity", "twilight sparkle"):
  print(image.url)
```

###Crawling Derpibooru from first to last image

```python
from derpibooru import Search

# This is only an example and shouldn't be used in practice as it abuses
# Derpibooru's licensing terms
for image in Search().ascending().image_limit(None):
  id, score, tags = image.id_number, image.score, ", ".join(image.tags)
  print("#{} - score: {:>3} - {}".format(id, score, tags))
```

###Getting random images

```python
from derpibooru import Search, sort

for image in Search().sort_by(sort.random):
  print(image.url)
```

###Getting top 100 posts
```python
from derpibooru import Search, sort

top_scoring = [image for image in Search().sort_by(sort.score).image_limit(100)]
```

###Storing and passing new search parameters

```python
from derpibooru import Search, sort

params = Search().sort_by(sort.score).image_limit(100).parameters

top_scoring = Search(**params)
top_animated = top_scoring.query("animated")
```

###Filtering by metadata

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
