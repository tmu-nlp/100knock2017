import sys
n=int(sys.argv[1])
file_num = 1
data = []

f=open('hightemp.txt', "r")
for i,line in enumerate(f):
#iとlineを繋げて表示
    data.append(line.strip())
#改行を消してdataに加える
    if(i+1) % n ==0:
        #%aは割り算の余り、↑余がゼロになったら書き込む
        with open('split{}.txt'.format(file_num), 'w') as f:
        #with as 勝手に閉じる　format file_numをつける
            f.write('\n'.join(data))
#↑改行でdataをつなぐ
        data = []
        file_num += 1
if len(data)>0:

    with open('split{}.txt'.format(file_num), 'w') as f:
        f.write('\n'.join(data))
#↑余の分を書き込む


