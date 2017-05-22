from knock20 import wiki_UK
import re

for line in wiki_UK().split('\n'):
    obj = re.findall(r'(==+)(.*?)==+', line)

    if obj:
        for i in obj:
            print(len(i[0])-1, i[1])

#i[0]は=の数。今回は==でレベル1のため、len()でとった長さから1を引く必要がある


# for line in wiki_UK().split('\n'):
#     if "===" in line:
#         print(line.strip("===").strip() + "2")
#     elif "==" in line:
#         print(line.strip("==").strip() + "1")
