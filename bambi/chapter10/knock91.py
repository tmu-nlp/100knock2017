def read(f):
    for l in open(f):
        yield l
excluded_flag = False
with open("model91.txt","w") as output:
    for line in read("questions-words.txt"):
        line = line.strip()
        if ":" in line:
            if line in ": family":
                excluded_flag = True
            else:
                excluded_flag = False
                
        if excluded_flag == False:
            print(line,file=output)
print("finished")
    
