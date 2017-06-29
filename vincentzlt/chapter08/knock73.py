
# coding: utf-8

# In[15]:


import os,random,pickle
import numpy as np
from pprint import pprint
from collections import defaultdict
import nltk
import sklearn
lemma = nltk.wordnet.WordNetLemmatizer()
logistic_rg=sklearn.linear_model.LogisticRegression()


# In[8]:


(labels,features)=pickle.load(file=open("features.pkl","rb"))


# In[11]:


w_ids={}
ws=[]
for feature in features:
    for w in feature:
        ws.append(w)
ws=set(ws)
for w in ws:
    w_ids[w]=len(w_ids)


# In[19]:


arrays=np.zeros((len(features),len(ws)))

for idx, feature in enumerate(features):
    for w in feature:
        arrays[idx][w_ids[w]]=feature[w]
    


# In[22]:


y=np.array(labels)


# In[23]:


y


# In[25]:


lg_learned=logistic_rg.fit(arrays,y)

