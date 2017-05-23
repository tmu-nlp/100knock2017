
# coding: utf-8

# In[2]:

#!/usr/bin/python

import sys, pprint, re,pickle
from collections import defaultdict


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


# In[9]:

def get_verb_surface(mecab_list):
    verb_list=[]
    for w in mecab_list:
        if w['品詞']=='動詞':
            verb_list.append(w['原形'])
    return verb_list


# In[10]:

if __name__ == "__main__":
    mecob_list=get_verb_surface(get_wordlist("./neko.txt.mecab"))
    
    print(len(mecob_list),mecob_list[:100],sep="\n")


# In[ ]:



