from knock30 import getMecab
data = [x["base"] for x in getMecab() if x["pos"] == '動詞']
print(data)
