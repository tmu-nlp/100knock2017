count_row = 0
with open('hightemp.txt', 'r') as f:
    for row in f:
        count_row += 1
print ('行数:%d' %(count_row))
"""
wc -l hightemp.txt
"""
