from derpibooru import sort

def test_sorting_methods():
  sorting_methods = {
    "created_at",
    "score",
    "relevance",
    "height",
    "comments",
    "random"
  }

  methods = sort.__dict__

  assert len(sorting_methods) == len(methods)
  assert sorting_methods == sort.methods

  for key, value in methods.items():
    assert key == value.upper()
