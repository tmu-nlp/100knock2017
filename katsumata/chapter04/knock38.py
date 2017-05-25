from knock36 import make_frequency_dict
from matplotlib import pyplot as plt
from collections import defaultdict
word_token = defaultdict(int)

frequency_dict = make_frequency_dict()
word_f_list = list()
for word,count in sorted(frequency_dict.items(), key = lambda x:x[1], reverse = True):
    word_f_list.append(count)
plt.hist(word_f_list, bins = 100, log = True)
plt.show()
