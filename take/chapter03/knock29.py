import re
from knock20 import gen_uk_info
import mwclient

m = re.findall(r'{{2}基礎情報([\s\S]+?)\n}{2}', gen_uk_info())
for i in m:
    result_dict = re.findall(r'^\|(.*?)\s=\s(.*?)(?:\n|<br/>\n)', i, flags=re.M|re.S)
    for k,v in result_dict:
        if k == '国旗画像':
            site = mwclient.Site('en.wikipedia.org')
            file = site.images[v]
            print(file.imageinfo['url'])
            break
