
# coding: utf-8

# In[1]:


import os,random
from pprint import pprint


# In[2]:


stopwords=open("./stopwords.txt","r",encoding="utf-8").readlines()


# In[3]:


def isstopword(w):
    if w in stopwords:
        return True
    else:
        return False

