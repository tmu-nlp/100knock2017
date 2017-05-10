f = open('hightemp.txt', 'r')
count = 0
for line in f:
    count += 1

print(count)
f.close()


#UNIXよくわからないので後で追加する
#wc -l hightemp.txt
