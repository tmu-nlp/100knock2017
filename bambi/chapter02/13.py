import os
with open("merge.txt","w") as output, open("col1.txt","r") as file1 , open("col2.txt","r") as file2:
    zipped = zip(file1.read().splitlines(),file2.read().splitlines())
    data = list(zipped)
    for tup in data:
        content = "{}\n".format("\t".join(tup))
        print(content)
        output.write(content)
print("確認")
os.system("paste col1.txt col2.txt")
