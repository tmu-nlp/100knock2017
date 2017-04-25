import os
with open("hightemp.txt") as file:
    lines = file.readlines()
    print(sorted(lines,key=lambda x: (x[2]),reverse=True))
print("確認")
os.system("sort -r -k  3,3 hightemp.txt")
