from knock30s import loadmecabdata

for i in loadmecabdata():
    for j in i:
        if j['pos'] == '動詞':
            print('動詞の表層系: ', j['surface'])