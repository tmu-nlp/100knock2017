
# coding: utf-8

# In[1]:


import word2vec,pickle
from itertools import chain
from pprint import pprint
from sklearn.cluster import KMeans


# In[5]:


countries_=pickle.load(open("./countries.pkl","rb"))


# In[6]:


countries=[countries_[c] for c in countries_]


# In[7]:


kmeans = KMeans(n_clusters=5, random_state=0).fit(countries)


# In[8]:


kmeans.labels_


# In[9]:


kmeans.cluster_centers_

