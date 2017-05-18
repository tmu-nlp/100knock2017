from knock20 import jsonget
import re

en = jsonget().split('\n')
for data in en:
    if 'Category' in data:
        data = re.sub(r'\S*:',"",data)
        data = re.sub(r']]',"",data)
        print(data)
