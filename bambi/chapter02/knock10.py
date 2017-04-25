import os
with open("hightemp.txt" ,"r") as file:
    print (len(file.readlines()))
print("確認：")
os.system("wc -l hightemp.txt")
