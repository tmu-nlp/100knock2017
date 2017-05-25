
# coding: utf-8

# In[16]:

#!/usr/bin/python

import sys, pprint, re,pickle,matplotlib
from collections import defaultdict
import matplotlib.pyplot as plt


# In[3]:

def get_wordlist(f_name):
    mecob_list = []

    for line in open(f_name, "r", encoding="UTF-8"):
        word_pos_dict = {}
        pos_ls = iter([
            "word", "品詞", "品詞細分類1", "品詞細分類2", "品詞細分類3", "活用型", "活用形", "原形", "読み",
            "発音"
        ])
        if not line.startswith("EOS"):
            word_, pos_ = line.replace("\n", "").split("\t")
            pos_ = pos_.split(",")
            len_pos = len(pos_)

            word_pos_dict[next(pos_ls)] = word_

            for i in pos_:
                word_pos_dict[next(pos_ls)] = i
            mecob_list.append(word_pos_dict)
    return mecob_list


# In[4]:

def get_freq(mecob_list):
    freq_dict=defaultdict(lambda:0)
    for w in mecob_list:
        freq_dict[w["word"]]+=1
    return freq_dict


# In[28]:

def print_graph(data):
    # data should be list of tuples, each tuple is a key-value pair
    n_groups=len(data)

    bar_hight=list(i[1] for i in data)
    bar_note=list(i[0] for i in data)
    
    
    plt.bar([i+1 for i in range(n_groups)],bar_hight,tick_label=bar_note, align="center")
    plt.show()


# In[6]:

# In[22]:

if __name__ == "__main__":
    freq_dict=get_freq(get_wordlist("./neko.txt.mecab"))
    freq_dict=sorted(freq_dict.items(), key=lambda d:d[1], reverse = True)
    
    print_graph(freq_dict[:10])


# In[ ]:



