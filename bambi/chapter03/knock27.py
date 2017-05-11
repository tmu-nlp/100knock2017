import re
from collections import OrderedDict
from knock26 import dataRemovedBoldMarkup
def dataRemoveLinkMarkup():
    data = dataRemovedBoldMarkup()
    result = OrderedDict()
    pattern = r"((\[\[)|(\]\]))"
    for key, value in data.items():
        modified_value = re.sub(pattern,r"",value)
        result[key] = modified_value
    return result
print(dataRemoveLinkMarkup())
