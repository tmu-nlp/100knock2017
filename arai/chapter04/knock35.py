from knock30 import mecab_data

Mlist = mecab_data()
nlist = []
Nlist = []
for line in Mlist:
    for line2 in line:
        if line2['pos']=='名詞':
            nlist.append(line2['surface'])
        else:
            if len(nlist)>0:
                Nlist.append(nlist)
            nlist = []
print(sorted(Nlist,key=lambda x:len(x))[-1])
