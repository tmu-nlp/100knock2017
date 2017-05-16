from knock30 import getMecab
data = [x["surface"] for x in getMecab() if x["pos1"] == 'サ変接続' and x["pos"] == '名詞']
print(data)
