from knock26 import ktemp
import re

def ltemp():
    dic = ktemp()
    for key in dic:
#        dic[key] = re.sub(r'(\/\/)|(\[\[.*\|)','',dic[key])
        dic[key] = re.sub(r'\[\[\w*\|', '', dic[key])
        dic[key] = re.sub(r'\[\[', '', dic[key])
        dic[key] = re.sub(r'\]\]', '', dic[key])
    return dic

if __name__ == '__main__':
    for key, data in sorted(ltemp().items()):
        print('{} : {}'.format(key, data))
