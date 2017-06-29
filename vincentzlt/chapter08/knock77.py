
# coding: utf-8

# In[18]:


import os,random,pickle
import numpy as np
from pprint import pprint
from collections import defaultdict
import nltk
import sklearn
from collections import Counter
lemma = nltk.wordnet.WordNetLemmatizer()
logistic_rg=sklearn.linear_model.LogisticRegression()


# In[29]:


lg_model=pickle.load(open("./lg_model.pkl","rb"))
labels,arrays=pickle.load(open("./arrays.pkl","rb"))


# In[30]:


predicted_labels=[]
for array in arrays:
    predicted_labels.append(lg_model.predict(array.reshape(1,-1)))


# In[31]:


predicted_labels=np.array(list([i[0] for i in predicted_labels]))


# In[27]:


f1=sklearn.metrics.f1_score(labels,predicted_labels,pos_label="+1")


# In[35]:


accuracy=sklearn.metrics.accuracy_score(labels,predicted_labels)


# In[37]:


recall=sklearn.metrics.recall_score(labels,predicted_labels,pos_label="+1")


# In[ ]:




