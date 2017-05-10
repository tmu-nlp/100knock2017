import json, re, string
from knock21 import getCategoryRawList, getEnglandArticle
england = getEnglandArticle()
content = getCategoryRawList(england)
content_str = "\n".join(content)
result = re.sub('[Category%s]' % re.escape(string.punctuation), '', content_str)
print(result)
