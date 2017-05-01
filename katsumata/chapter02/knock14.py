row_n = input('行数:')
with open('hightemp.txt', 'r') as f:
    row =  list(f)
    for i in range(int(row_n)):
        print(row[i].strip())
#head -n 4 hightemp.txt
