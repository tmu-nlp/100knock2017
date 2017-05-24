from knock30 import mecab_data
from collections import defaultdict
import matplotlib.pyplot as plt

word_counts = defaultdict(lambda: 0)

Mlist = mecab_data()

for line in Mlist:
    for word in line:
        word_counts[word['surface']] +=1

    
numberlist = list(word_counts.values())    

plt.hist(numberlist,bins=200)
plt.show()
