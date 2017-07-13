
# coding: utf-8

# In[9]:


import word2vec
from pprint import pprint


# In[3]:


model=word2vec.load("./enwiki-20150112-400-r10-105752.bin")


# In[12]:


for line in open("./family.txt","r",encoding="utf-8"):
    if not line.startswith(": "):
        w1,w2,w3,w4=line.split()
        try:
            idx, metrics=model.analogy(pos=[w2,w3],neg=[w1],n=10)
            print("+ {} {} - {}".format(w2,w3,w1))
            pprint(model.generate_response(idx,metrics).tolist())
            print()
        except KeyError:
            pass

