import os
N = int(input("Please enter N ="))
with open("hightemp.txt") as file:
    print("".join(file.readlines()[-N:]))
print("確認")
os.system("tail -n {} hightemp.txt".format(N))
