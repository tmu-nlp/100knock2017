f = open('hightemp.txt', 'r')
#和歌山県葛城のところが謎に開くのを直したいけどよくわからない
N = int(input())
count = 0

for line in f:
    if count % N == 0:
        print()
        #　N行を出力？したところで、空白の行を入れる
    print(line, end="")
    count += 1

f.close()
