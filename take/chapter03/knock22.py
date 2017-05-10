import re
from knock20 import gen_uk_info
catName = re.findall(r'\[\[Category:(.*)\]\]', gen_uk_info())
for c in catName:
    print(c)