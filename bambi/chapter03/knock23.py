import re
from knock21 import getEnglandArticle
content = getEnglandArticle()
if content:
    #例えば"== セクション名 =="なら1　。。。もう適当
    data = re.findall(r"==.*",content)
    modified_data = {(int(x.count("=")/2 - 1), x.replace("=","").strip()) for x in data}
    for key, item in modified_data:
        print("{0} {1}".format(item,key))
