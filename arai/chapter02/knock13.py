f1=open('col1.txt', "r")
f2=open('col2.txt', "r")
f3=open('col3.txt', "a")
for y,w in zip(f1,f2):
    y = y.rstrip("\n")
    w = w.rstrip("\n")
    f3.write(y+"\t"+w+"\n")
