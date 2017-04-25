import os
with open("hightemp.txt") as file:
    lines = file.readlines()
    first_column_list = [x.split("\t")[0] for x in lines]
    print(sorted(set(first_column_list)))
print("確認")
os.system("cut -f 1 hightemp.txt | sort | uniq")
