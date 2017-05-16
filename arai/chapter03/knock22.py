from knock20 import getUK 
import re

for line in getUK():
    matchobj = re.findall(r'\[\[Category:(.*?)\|*\**\]\]',line)
    if matchobj:
        for m in matchobj:
            print(m)  

    

