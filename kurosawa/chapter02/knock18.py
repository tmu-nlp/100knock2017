with open('hightemp.txt','r') as f:
    col = []
    for list in f:
        list = list.split()
        col.append(list)
for i in sorted(col, key=lambda temp: temp[2]):
    print("%s\t%s\t%s\t%s" %(i[0],i[1],i[2],i[3]))

