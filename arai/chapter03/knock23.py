from knock20 import getUK
import re

for line in getUK():
    matchobj = re.findall(r'(==+)(.*?)==+',line)

    if matchobj:
        for m in matchobj:
            print(len(m[0])-1,m[1])
