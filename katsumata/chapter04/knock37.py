from knock36 import make_frequency_dict
from matplotlib import pyplot as plt
frequency_dict = make_frequency_dict()
word_list = list()
count_list = list()
word_num_list = list()
counter = 0
for word, count in sorted(frequency_dict.items(), key = lambda x:x[1], reverse = True):
    word_list.append(word)
    count_list.append(count)
    counter += 1
    if counter == 10:
        break
for i, word in enumerate(word_list):
    word_num_list.append(i)
plt.bar(word_num_list, count_list)
plt.xticks(word_num_list, word_list)
plt.show() 
