from knock20 import wiki_UK
import re

for line in wiki_UK().split('\n'):
    obj = re.findall(r'ファイル:(.*?)\|', line)

    if obj:
        for i in obj:
            print(obj)
