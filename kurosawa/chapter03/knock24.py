from knock20 import jsonget
import re

en = jsonget().split('\n')
for data in en:
    if 'ファイル' in data:
        data = re.sub(r'\S*ファイル:',"",data)
        data = re.sub(r'\|国章画像 = ','',data)
        print(re.sub(r'\|.*',"",data))

