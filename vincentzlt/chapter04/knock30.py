
# coding: utf-8

# In[1]:

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys, pprint, re,pickle
from collections import defaultdict


# In[10]:

mecob_list = []

for line in open("./neko.txt.mecab", "r", encoding="UTF-8"):
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


# In[16]:

pickle.dump(mecob_list,open("word_mapping.mecab","wb"))


# In[ ]:



