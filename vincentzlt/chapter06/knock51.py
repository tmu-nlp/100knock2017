
# coding: utf-8

# In[2]:

import sys,re


# In[60]:

def sentence_break(f_name):
    for line in open(f_name, "r",encoding="utf-8"):
        #print(line)
        rg_str=r"([\.\;\:\?\!]) ([A-Z])"
        subbed_line=re.sub(rg_str,r"\1\n\2",line)
        for l in subbed_line.split("\n"):
            if l:
                yield l
        


# In[94]:

def word_segmentation(sentence):
    #(print(sentence)
    for w in sentence.split():
        subbed_w=re.finditer("\w+",w)
        if subbed_w:
            for i in list(subbed_w):
                yield i.group(0)


# In[95]:

for ind,sent in enumerate(sentence_break("./nlp.txt")):
    for ind, w in enumerate(word_segmentation(sent)):
        print(w)


# In[ ]:



