
# coding: utf-8

# In[6]:


import os,random,pickle
import numpy as np
from pprint import pprint
from collections import defaultdict
import nltk
import sklearn
from collections import Counter
lemma = nltk.wordnet.WordNetLemmatizer()
logistic_rg=sklearn.linear_model.LogisticRegression()


# In[13]:


lg_model=pickle.load(open("./lg_model.pkl","rb"))
w_ids=pickle.load(open("./w_ids.pkl","rb"))


# In[31]:


rank=lg_model.coef_.argsort()


# In[34]:


for i in range(10):
    for idx,w in enumerate(w_ids):
        if w_ids[w]==rank[0][i]:
            print(w)


# In[35]:


for i in range(10):
    for idx,w in enumerate(w_ids):
        if w_ids[w]==rank[0][-i]:
            print(w)

