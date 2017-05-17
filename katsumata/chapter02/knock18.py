count = 0
with open('hightemp.txt', 'r') as f:
    rows = list()
    for row in f:
        rows.append(row.split())
        count += 1
    s_row = sorted(rows, key = lambda x:float(x[2]))
    for i in range(count):
        for word in s_row[i]:
            print (word,end='\t')
        print ('')
#sort -k 3,3 -n hightemp.txt
