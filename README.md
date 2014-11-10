# DerPyBooru

Python bindings for Derpibooru's API

License: **Simplified BSD License**

## Dependencies

- python2.7 or newer
- requests

## How to install

    pip install https://github.com/joshua-stone/pyderpibooru/zipball/master

##Typical usage

###Crawling Derpibooru's front page

```python
from derpibooru import Search

for image in Search():
  print(image.url)
```

###Searching by tag

```python
from derpibooru import Search

for image in Search().query("rarity", "safe"):
  print(image.url)
```

###Crawling Derpibooru from first to last image

```python
from derpibooru import Search

for image in Search().ascending():
  print(image.url)
```

###Getting random images

```python
from derpibooru import Search

for image in Search().sort_by("random")
  print(image.url)
```
