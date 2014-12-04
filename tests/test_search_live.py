from derpibooru import Search

def test_query():
  """
  Tests whether the results in a query contain the tag that was being searched
  for
  """
  limit, tag = 10, "sunset shimmer"
  images = [image for image in Search().query(tag).limit(limit)]

  assert len(images) == limit

  for image in images:
    assert tag in image.tags

def test_ascending():
  """
  Tests whether ascending search is in the correct order
  """
  limit = 10
  images = [image for image in Search().ascending().limit(limit)]

  assert len(images) == limit

  for image in images:
    # Check if the images are in ascending order
    # by comparing the ID of the next image 
    if image is not images[-1]:
      next_image = images[images.index(image) + 1]
      assert image.id_number < next_image.id_number

def test_descending():
  """
  Tests whether descending search is in the correct order
  """
  limit = 10
  images = [image for image in Search().descending().limit(limit)]

  assert len(images) == limit

  for image in images:
  # Check if the image IDs are listed in descending order
  # by comparing the ID of the next image
    if image is not images[-1]:
      next_image = images[images.index(image) + 1]
      assert image.id_number > next_image.id_number

