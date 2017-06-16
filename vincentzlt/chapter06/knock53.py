
# coding: utf-8

# In[1]:

import sys,re,pdir
from stemming.porter2 import stem
from lxml import etree


# In[2]:



# In[25]:

def tokenization_corenlp(f_name):
    tree=etree.parse(f_name)
    root=tree.getroot()
    words=root.xpath("//word")
    for w in words:
        print(w.text)


# In[27]:
if __name__=="__main__":
    tokenization_corenlp("./nlp_sentence_break.txt.xml")


# In[10]:


# In[ ]:



