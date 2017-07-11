
# coding: utf-8

# In[3]:


import time,re,time,random,math
from sklearn.decomposition import PCA
from collections import Counter
import pickle


# In[2]:


f_name="./enwiki-20150112-400-r10-105752.txt.token.contry_name.contexts"


# In[3]:


ppmis=pickle.load(file=open(f_name,"rb"))


# In[ ]:


pca_ppmis=PCA(n_components=300)


# In[ ]:


with open(f_name+".pca","wb") as f_out:
    pickle.dump(pca_ppmis,f_out)

