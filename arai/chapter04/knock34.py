from knock30 import mecab_data

Mlist = mecab_data()
for line in Mlist:
    for i,line2 in enumerate(line):
        if line2['pos']=='名詞' and line[i-1]['surface']=='の' and line[i-2]['pos']=='名詞':
             print(line[i-2]['surface']+line[i-1]['surface']+line2['surface'])
