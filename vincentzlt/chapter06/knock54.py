
# coding: utf-8

# In[1]:

import sys,re,pdir
from stemming.porter2 import stem
from lxml import etree




# In[32]:

def pos_tagging(f_name):
    tree=etree.parse(f_name)
    root=tree.getroot()
    tokens=root.xpath("//token")
    for w in tokens:
        output=[]
        for w_ in w:
            if w_.tag=="word":
                output.append(w_.text)
            if w_.tag=="lemma":
                output.append(w_.text)
            if w_.tag=="POS":
                output.append(w_.text)
        print("\t".join(output))


# In[33]:

pos_tagging("./nlp_sentence_break.txt.xml")


# In[ ]:



