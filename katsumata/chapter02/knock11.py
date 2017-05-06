with open('hightemp.txt', 'r') as f:
    for row in f:
        row = row.replace('\t', ' ')
        print (row.strip())
#cat hightemp.txt | tr '\t' ' '
