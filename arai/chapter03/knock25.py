from knock20 import getUK
import re

flag = False
for line in getUK():
    if line.startswith('{{基礎情報'):
        flag = True
    elif flag == True and line.startswith('}}'):
        break
    elif flag == True:
        matchobj=re.findall(r'\|(.*?)=(.*)',line)
        if matchobj:
            for m in matchobj:
                print(m)
            
            
