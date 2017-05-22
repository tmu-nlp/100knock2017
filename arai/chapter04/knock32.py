from knock30 import mecab_data

Mlist = mecab_data()
for line in Mlist:
    for line2 in line:
        if line2['pos']=='動詞':
            print(line2['base'])
