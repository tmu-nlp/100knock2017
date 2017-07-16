
# coding: utf-8

# In[1]:


import word2vec
from itertools import chain
from pprint import pprint
import pickle


# In[2]:


model=word2vec.load("./enwiki-20150112-400-r10-105752.bin")


# In[3]:


countries = {}
correct = []
for idx, line in enumerate(
        chain(
            open("./country_names", "r", encoding="utf-8"),
            open("./country_names_with_space","r",encoding="utf-8"))):
    line=line.strip()
    try:
        countries[line]=model[line]
    except KeyError:
        pass
pickle.dump(countries,open("./countries.pkl","wb"))

