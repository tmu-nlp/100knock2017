from knock30 import mecab_data
from collections import defaultdict

word_counts = defaultdict(lambda: 0)
Mlist = mecab_data()

for line in Mlist:
    for word in line:
        word_counts[ word['surface']] += 1
       
        

for y,w in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    print(y,w)


