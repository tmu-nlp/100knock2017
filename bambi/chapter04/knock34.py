from knock30 import getMecab
items = getMecab()
for index, x in enumerate(items):
        if x["surface"] == "の":
            if items[index -1]["pos"] == "名詞" and items[index +1]["pos"] == "名詞":
                print("{}{}{}".format(items[index-1]["surface"],items[index]["surface"],items[index+1]["surface"]))
    
