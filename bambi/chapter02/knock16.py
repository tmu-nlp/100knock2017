import os
N = int(input("Please enter N ="))
count = 0
file_no = 1
with open("hightemp.txt", "r") as file:
    lines = file.read().splitlines()
    while count < len(lines):
        with open("file{}.txt".format(file_no), "w", encoding="utf8") as output:
            for x in lines[count:count+N]:
                content = "{}\n".format(x)
                print(content)
                output.write(content)
            print("//////")
            count += N
            file_no += 1
print("確認")
os.system("split -l {} hightemp.txt".format(N))
