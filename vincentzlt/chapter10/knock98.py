
# coding: utf-8

# In[1]:


import word2vec,pickle
from itertools import chain
from pprint import pprint
from sklearn.cluster import AgglomerativeClustering


# In[2]:


countries_=pickle.load(open("./countries.pkl","rb"))


# In[3]:


countries=[countries_[c] for c in countries_]


# In[4]:


ward = AgglomerativeClustering(n_clusters=5).fit(countries)


# In[5]:


ward.labels_


# In[7]:


ward.n_components_

