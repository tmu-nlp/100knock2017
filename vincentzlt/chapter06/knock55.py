
# coding: utf-8

# In[1]:

import sys,re,pdir
from stemming.porter2 import stem
from lxml import etree


# In[34]:

def named_entity_extraction(f_name):
    tree=etree.parse(f_name)
    root=tree.getroot()
    tokens=root.xpath("//token")
    for w in tokens:
        for w_ in w:
            if w_.tag=="word":
                output=w_.text
            if w_.tag=="POS":
                if w_.text=="NNP":
                    print(output)
    
                


# In[35]:

named_entity_extraction("./nlp_sentence_break.txt.xml")

