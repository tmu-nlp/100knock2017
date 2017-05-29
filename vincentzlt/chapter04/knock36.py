
# coding: utf-8

# In[3]:

#!/usr/bin/python

import sys, pprint, re,pickle
from collections import defaultdict


# In[4]:

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
            #len_pos = len(pos_)

            word_pos_dict[next(pos_ls)] = word_

            for i in pos_:
                word_pos_dict[next(pos_ls)] = i
            mecob_list.append(word_pos_dict)
    return mecob_list


# In[17]:

def get_freq(mecob_list):
    freq_dict=defaultdict(lambda:0)
    for w in mecob_list:
        freq_dict[w["word"]]+=1
    return freq_dict


# In[22]:

if __name__ == "__main__":
    freq_dict=get_freq(get_wordlist("./neko.txt.mecab"))
    freq_dict=sorted(freq_dict.items(), key=lambda d:d[1], reverse = True)
    pprint.pprint(freq_dict)
    


# In[ ]:



