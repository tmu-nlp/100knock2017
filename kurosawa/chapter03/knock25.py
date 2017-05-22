from knock20 import jsonget
import re

def kisotemp():
    en = jsonget().split('\n')
    old = list()
    bag = str()
    dic = dict()
    flag = 0
    for data in en:
        if '基礎情報' in data:
            flag = 1
        elif re.match('}}',data):
            flag = 0
        elif flag == 1:
            data = re.sub(r'^\|','',data)
            data = re.sub(r'^\*+','',data)
#            print(data)
            data = re.split(r' *= *',data)
            data.append('')
            if data[1] is '':
                data[1] = old + ' & ' + data[0]
                data[0] = bag
            dic[data[0]] = data[1]
            bag = data[0]
            old = data[1]
#            print(old)
#    print(dic)
    return dic

if __name__ == '__main__':
    for key, data in sorted(kisotemp().items()):
        print('{} : {}'.format(key,data))
