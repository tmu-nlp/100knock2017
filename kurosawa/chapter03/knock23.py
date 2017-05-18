from knock20 import jsonget
import re

en = jsonget().split('\n')
for data in en:
    datanew = re.search(r'^=+\S*=+$', data)
    if datanew != None:
        print(re.sub(r'=*',"",data), end=' ')
        print(int(data.count('=')/2-1))

