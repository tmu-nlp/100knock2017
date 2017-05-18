with open('hightemp.txt','r') as f:
    col = []
    for list1 in f:
        list1 = list1.split()
        col.append(list1)
for i in sorted(col, key=lambda temp: temp[2]):
    print("%s\t%s\t%s\t%s" %(i[0],i[1],i[2],i[3]))

# sort -k3 hightemp.txt
