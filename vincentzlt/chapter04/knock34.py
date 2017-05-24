
# coding: utf-8

# In[2]:

#!/usr/bin/python

import sys, pprint, re,pickle
from collections import defaultdict


# In[22]:

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


# In[27]:

def get_no(mecab_list):
    verb_list=[]
    for w in list(zip(mecab_list[:-2],mecab_list[1:-1],mecab_list[2:])):
        #pprint.pprint(w)
        if w[0]['品詞']=='名詞' and w[1]['word']=='の' and w[1]['品詞']=='助詞' and w[2]['品詞']=='名詞':
            verb_list.append([w[0]['word'],w[1]['word'],w[2]['word']])
    return verb_list


# In[30]:

if __name__ == "__main__":
    word_list=get_no(get_wordlist("./neko.txt.mecab"))
    for w in word_list:
        print("".join(w))
    


# In[ ]:



