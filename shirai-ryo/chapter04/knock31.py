from knock30 import nekoneko

for line in nekoneko():
    for i in line:
        print(i["surface"])

        #ダメだったやつ
        # print(line[i]["surface"])
