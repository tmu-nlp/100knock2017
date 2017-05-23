from knock36 import make_frequency_dict
from matplotlib import pyplot as plt

frequency_dict = make_frequency_dict()
word_f_list = list()
word_list = list()
word_num_list = list()

for word, count in sorted(frequency_dict.items(), key = lambda x:x[1], reverse = True):
    word_f_list.append(count)
    word_list.append(word)
for i, word in enumerate(word_list):
    word_num_list.append(i)
plt.xscale('log')
plt.yscale('log')
plt.plot(word_num_list, word_f_list)
plt.show()
