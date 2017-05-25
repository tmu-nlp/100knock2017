from knock30 import mecab_data
from collections import defaultdict
import matplotlib.pyplot as plt

word_counts = defaultdict(lambda: 0)
Mlist = mecab_data()
wordlist = []
countlist = []
numberlist = []
for line in Mlist:
    for word in line:
        word_counts[ word['surface']] += 1
       
        
i = 0
for y,w in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    wordlist.append(y)
    countlist.append(w)
    numberlist.append(i)
    i += 1

plt.xscale("log")
plt.yscale("log")
plt.plot(numberlist, countlist)
plt.show()

