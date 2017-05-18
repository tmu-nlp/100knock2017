import re, string
from collections import OrderedDict
from knock27 import dataRemoveLinkMarkup

class EnglandContent(object):
    def removeMarkup(self, content):
        return re.sub('%s' % re.escape(string.punctuation), '', content)
    '''
        content = re.sub(r'<.*?>', r"", content)
        content = re.sub(r'(==+)', r"", content)
        content = re.sub(r'\{\{|\}\}', r"", content)
        content = re.sub(r'\[|\]', r"", content)
        content = re.sub(r'(#+)|\;|(\*+)', r"", content)
        return content
    '''
    def getItem(self):
        data = dataRemoveLinkMarkup()
        result = OrderedDict()
        for k, v in data.items():
            new_v = self.removeMarkup(v)
            new_k = k.replace(" ", "")
            result[new_k] = new_v
        return result


result = EnglandContent().getItem()

print(result)
