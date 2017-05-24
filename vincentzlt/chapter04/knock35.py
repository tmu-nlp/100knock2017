
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
            len_pos = len(pos_)

            word_pos_dict[next(pos_ls)] = word_

            for i in pos_:
                word_pos_dict[next(pos_ls)] = i
            mecob_list.append(word_pos_dict)
    return mecob_list


# In[14]:

def get_NNN(mecab_list):
    noun_list=[]
    nn=[]
    
    n_in=False
    
    for w in mecab_list:
        if (w["品詞"]=="名詞") and (not n_in):
            nn=[]
            nn.append(w["word"])
            n_in=True
        elif w["品詞"]=="名詞" and  n_in:
            nn.append(w["word"])
        elif w["品詞"]!="名詞" and n_in:
            if len(nn)>1:
                noun_list.append(nn)
            n_in=False
        else:
            n_in =False
        
    return noun_list


# In[16]:

if __name__ == "__main__":
    word_list=get_NNN(get_wordlist("./neko.txt.mecab"))
    for nn in word_list:
        print("".join(nn))
    


# In[ ]:



