from knock20 import getUK 
import re

for line in getUK():
    matchobj = re.search(r'\[\[Category.*',line)
    if matchobj:
        print(line)  

    

