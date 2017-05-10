text = open('hightemp.txt', 'r')
count = 0
for str in text:
    count += 1

print'count:', count
text.close()
