import re
from collections import OrderedDict
from knock25 import getInformationDict
def dataRemovedBoldMarkup():
    data = getInformationDict()
    result = OrderedDict()
    pattern = r"([(\'\')|(\'\'\')|(\'\'\'\'\')])"
    for key, value in data.items():
        new_value = re.sub(pattern,r"",value)
        result[key] = new_value
    return result
print(dataRemovedBoldMarkup())
