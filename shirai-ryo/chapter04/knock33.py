from knock30 import nekoneko

for line in nekoneko():
    for i in line:
        if i["pos1"] == "サ変接続":
            print(i["surface"])
