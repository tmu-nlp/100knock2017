from knock20 import getUK
import re

d = {}

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
                mm = re.sub(r'["""]',"",m[1])
                mm = re.sub(r'["""""]',"",mm)
                mm = re.sub(r'[\[\[]',"",mm)
                mm = re.sub(r'[\]\]]',"",mm)
                d[m[0]]=mm
for key,value in sorted(d.items()):
    print(key,value)

            
            
