import re
from knock20 import gen_uk_info

m = re.findall(r'{{2}基礎情報([\s\S]+?)\n}{2}', gen_uk_info())
for i in m:
    result_dict   = re.findall(r'\n|(.*?)\s=\s(.*?)\n\|', i, flags=re.M|re.S)
    for k,v in result_dict:
        print(v)
        m = re.sub(r"\'{2,6}", '' ,v)
        print(m)
