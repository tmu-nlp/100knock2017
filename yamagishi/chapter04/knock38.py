from knock30 import get_morphs
from collections import defaultdict
import matplotlib.pyplot as plt

word_frequency = defaultdict(int)
for sentence in get_morphs('./neko.txt.mecab'):
    for word in sentence:
        word_frequency[word['base']] += 1

freq_frequency = defaultdict(int)
for key, value in word_frequency.items():
    freq_frequency[value] += 1

plt.hist(list(word_frequency.values()), bins=range(len(freq_frequency)))
plt.savefig('knock38_result.png')
plt.show()
