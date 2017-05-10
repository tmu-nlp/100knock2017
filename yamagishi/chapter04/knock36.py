from knock30 import get_morphs
from collections import defaultdict

frequency = defaultdict(int)
for sentence in get_morphs('./neko.txt.mecab'):
    for word in sentence:
        frequency[word['base']] += 1

for word, freq in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
    print(word, freq)
