row_n = input('行数:')
count_row = 0
with open('hightemp.txt', 'r') as f:
    for lin in f:
        count_row += 1
with open('hightemp.txt', 'r') as f2:
    row = list(f2)
    num_roop = int(row_n)
    count_first = count_row - num_roop
    for i in list(range(count_first,count_row)):
       print(row[i].strip())
#tail -n 4 hightemp.txt
