from knock30 import mecab_data
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname = '/System/Library/Fonts/AquaKana.ttc')

word_counts = defaultdict(lambda: 0)
Mlist = mecab_data()
wordlist = []
countlist = []
numberlist = []
for line in Mlist:
    for word in line:
        word_counts[ word['surface']] += 1
       
        
i = 0
for y,w in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    wordlist.append(y)
    countlist.append(w)
    numberlist.append(i)
    i += 1

plt.bar(numberlist, countlist)
plt.xticks(numberlist, wordlist, fontproperties = fp)
plt.show()

