from knock30 import nekoneko
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math

fp = FontProperties(fname='/System/Library/Fonts/AquaKana.ttc')

my_dict = defaultdict(int)

for line in nekoneko():
    for i in line:
        my_dict[i['base']] += 1

word_list = []
count_list = []
memori = []
count = 0
for k, v in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
    word_list.append(k)
    count_list.append(v)
    memori.append(count)
    count += 1

# print(word_list)
# print(count_list)
# print(memori)
# print(count)

plt.xscale('log')
plt.yscale('log')
plt.plot(memori, count_list)
plt.show()
