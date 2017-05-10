from knock30 import get_morphs
from collections import defaultdict
import matplotlib.pyplot as plt

frequency = defaultdict(int)
for sentence in get_morphs('./neko.txt.mecab'):
    for word in sentence:
        frequency[word['base']] += 1

plt.xscale('log')
plt.yscale('log')
plt.bar(range(1, len(frequency.values()) + 1), list(sorted(frequency.values(), reverse=True)))
plt.savefig('knock39_result.png')
plt.show()
