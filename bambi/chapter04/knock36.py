from collections import Counter
from knock30 import getMecab
def getOrderedFreqList():
    data = [x["surface"] for x in getMecab()]
    freq = Counter(data)
    return sorted(freq.items(), key=lambda i: i[1], reverse=True)
if __name__ == "__main__":
    print(getOrderedFreqList())
