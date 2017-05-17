import os

with open("hightemp.txt") as file:
    lines = file.readlines()
    print(sorted(lines,key=lambda x: float(x.split()[2])))
print("確認")
os.system("sort -n -k  3,3 hightemp.txt")
