import re
from collections import OrderedDict
from knock21 import getEnglandArticle
def getInformationDict():
    data = re.split(r'\n[\|}]',getEnglandArticle()) # set of \ or } to split
    result_dict = OrderedDict()
    for x in data:
        content = x.split("=",1)
        if len(content) == 2:
            result_dict[content[0]] = content[1]
    
    return result_dict
        
print(getInformationDict())
