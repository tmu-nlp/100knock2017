from knock30 import get_morphs
from collections import defaultdict
import matplotlib.pyplot as plt

frequency = defaultdict(int)
for sentence in get_morphs('./neko.txt.mecab'):
    for word in sentence:
        frequency[word['base']] += 1

plt.xscale('log')
plt.yscale('log')
plt.plot(range(len(frequency.values())), list(sorted(frequency.values(), reverse=True)))
plt.savefig('knock39_result.png')
plt.show()
