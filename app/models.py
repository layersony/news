class source:
  def __init__(self, id, name, description, category, url):
    self.id = id
    self.name = name
    self.description = description
    self.category = category
    self.url = url

class Article:
  def __init__(self, author, title, description, urlimg, published):
    self.author = author
    self.title = title
    self.description = description
    self.urlimg = urlimg
    self.published = published