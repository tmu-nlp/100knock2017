with open('hightemp.txt', 'r') as f:
    prefecture = set()
    for row in f:
        row = row.split()
        prefecture.add(row[0])
    for p in prefecture:
        print(p)   
#sort col1.txt | uniq 
