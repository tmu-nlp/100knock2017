f = open("hightemp.txt", 'r')
place = set()
#set()は空集合のこと

for line in f:
    lines = line.split()
    place.add(lines[0])
    #setに要素を追加する時はadd()
    #（おまけ）削除する時はremove()でできる
for i in place:
    print(i)
