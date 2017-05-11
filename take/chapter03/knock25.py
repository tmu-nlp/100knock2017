import re
from knock20 import gen_uk_info

m = re.findall(r'{{2}基礎情報([\s\S]+?)\n}{2}', gen_uk_info())
for i in m:
    resltdict = re.findall(r'\n|(.*?)\s=\s(.*?)\n\|', i, flags=re.M|re.S)
    for l in resltdict:
        print(l)
