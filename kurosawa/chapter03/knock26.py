from knock25 import kisotemp
import re

def ktemp():
    dic = kisotemp()
    for key in dic:
        dic[key] = re.sub(r'\'+','',dic[key])
    return dic

if __name__ == '__main__':
    for key,data in sorted(ktemp().items()):
        print('{} : {}'.format(key,data))
