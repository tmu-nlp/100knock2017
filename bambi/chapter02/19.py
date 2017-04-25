import os
from operator import itemgetter
from collections import Counter
with open("hightemp.txt") as file:
    lines = file.readlines()
    first_column_list = [x.split("\t")[0] for x in lines]
    frequency_list = Counter(first_column_list)
    data = frequency_list.most_common()
    data.sort(key=lambda tup: tup[0], reverse=True) # sorted name
    data.sort(key=lambda tup: tup[1], reverse=True) # sorted freq.
    for item in data:
        print("{} {}".format(item[1], item[0]))
print("確認")
os.system("cut -f 1 hightemp.txt | sort -r | uniq -c | sort -r")
