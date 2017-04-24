import os
with open("hightemp.txt" ,"r") as file:
    print(file.read().replace('\t',' '))
print("確認：")
os.system("sed 's/\t/ /g' hightemp.txt")
