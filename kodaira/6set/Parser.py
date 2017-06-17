import bs4


class KnockSoup(bs4.BeautifulSoup):
  """
    extend beatifulsoup for NLP100KNOCK
  """
  def __init__(self, fname):
    super(KnockSoup, self).__init__(open(fname), "html5lib")

  def extract_tokens(self, prev_content=None, get_func=(lambda x: x),
                     tags=["sentences", "sentence", "tokens", "token"]):
    xs = list()
    prev_content = prev_content or self

    tag, tags = tags[0], tags[1:]
    for content in prev_content.find_all(tag):
      if tags == []:
        xs.append(get_func(content))
      else:
        xs.append(self.extract_tokens(content, get_func, tags))
    return xs

