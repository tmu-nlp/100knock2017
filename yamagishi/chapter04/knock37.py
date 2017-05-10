from knock30 import get_morphs
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

frequency = defaultdict(int)
for sentence in get_morphs('./neko.txt.mecab'):
    for word in sentence:
        frequency[word['base']] += 1

x_data = list()
y_data = list()
for word, freq in sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:10]: 
    x_data.append(word)
    y_data.append(freq)

fp = FontProperties(fname='/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc')
plt.bar(range(len(x_data)), y_data)
plt.xticks(np.arange(len(x_data)) + 0.4, x_data, fontproperties=fp)
plt.savefig('knock37_result.png')
plt.show()
