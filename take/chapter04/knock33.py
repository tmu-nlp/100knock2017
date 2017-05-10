from knock30s import loadmecabdata

sahenlist = []
for i in loadmecabdata():
    for j in i:
        if j['pos'] == 'サ変接続':
            print("posがサ変接続の原型: ", j['base'])
        elif j['pos1'] == 'サ変接続':
            print("pos1がサ変接続の原型: ", j['base'])
            sahenlist.append(j['base'])

print(set(sahenlist))
print(len(sahenlist))
print(len(set(sahenlist)))
