import re
from knock21 import getEnglandArticle
data = getEnglandArticle()
content = re.findall(r'\[\[(ファイル|Media|File)\:(.*)?\|',data)
for key, item in content:
    result = item.split("|")[0]
    print(result)
