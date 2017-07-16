
# coding: utf-8

# In[16]:


import word2vec,pickle
from itertools import chain
from pprint import pprint
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
get_ipython().magic('matplotlib inline')


# In[2]:


countries_=pickle.load(open("./countries.pkl","rb"))


# In[3]:


countries=[countries_[c] for c in countries_]


# In[6]:


model=TSNE(n_components=3,random_state=0)
np.set_printoptions(suppress=True)


# In[12]:


plt_data=model.fit_transform(countries)
plt_data


# In[18]:


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(plt_data.T[0],plt_data.T[1],plt_data.T[2],alpha=0.4,s=10)

