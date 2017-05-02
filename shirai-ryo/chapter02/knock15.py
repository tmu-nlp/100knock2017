f = open('hightemp.txt')
N = int(input())

lines = f.readlines()
length = len(lines)
f.close()

#上で一回閉じないでやったらできなくて、閉じたらできたけど、なんでか不明なので聞く

f = open('hightemp.txt')
count = 0
for line in f:
    if count < length - N:
        count += 1
    else:
        print(line)

f.close()
