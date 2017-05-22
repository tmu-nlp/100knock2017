
import re, json
from collections import OrderedDict
from knock21 import getEnglandArticle
#"{{基礎情報 国\n|略名 = オーストリア\n|日本語国名 = オーストリア共和国\n|公式国名 =

# actually should do with group rex but lazy to change...
def getInformationDict():
    result_dict = OrderedDict()
    data = getEnglandArticle()
    start = False
    for line in data.split('\n'):
        if line.startswith("{{基礎情報"):
            start = True
        if start == True:
            dic = line.split("=")
            if len(dic) > 1:
                dic[0] = dic[0].replace("|","") # remove | in front of word
                result_dict[dic[0]] = dic[1]
            if line.startswith("}}"):
                break
    return result_dict

print(getInformationDict())




# In[ ]:
