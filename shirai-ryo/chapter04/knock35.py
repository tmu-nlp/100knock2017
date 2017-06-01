from knock30 import nekoneko

champion = []

for line in nekoneko():
    word_count = []
    for i in line:
        if i['pos'] == '名詞':
            word_count.append(i['surface'])
        else:
            if len(champion) <= len(word_count):
                champion = word_count
            word_count = []

print(champion)
