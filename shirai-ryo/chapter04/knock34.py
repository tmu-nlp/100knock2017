from knock30 import nekoneko

for line in nekoneko():
    for count, i in enumerate(line[:-1]):
        if i['surface'] == 'の':
            if line[count-1]['pos'] == '名詞' and line[count+1]['pos'] == '名詞':
                print(line[count-1]['surface'] + 'の' + line[count+1]['surface'])
