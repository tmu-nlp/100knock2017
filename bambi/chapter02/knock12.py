import os
with open("hightemp.txt","r") as file, open("col1.txt","w") as output1 , open("col2.txt","w") as output2:
    for line in file.readlines():
        columns = line.split('\t')
        first_column = columns[0] + "\n"
        output1.write(first_column)
        print(first_column)
        second_column = columns[1] + "\n"
        output2.write(second_column)
        print(second_column)
print("確認：")
os.system("cut -f 1 col1.txt")
os.system("cut -f 2 col2.txt")
