from knock30 import getMecab
data = [x["surface"] for x in getMecab() if x["pos"] == '動詞']
if __name__ == "__main__":
    print(data)
