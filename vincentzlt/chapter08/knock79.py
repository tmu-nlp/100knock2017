
# coding: utf-8

# In[11]:


import os,random,pickle
import numpy as np
from pprint import pprint
from collections import defaultdict
import nltk
import sklearn
from collections import Counter
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
lemma = nltk.wordnet.WordNetLemmatizer()
logistic_rg=sklearn.linear_model.LogisticRegression()


# In[2]:


labels,arrays=pickle.load(open("./arrays.pkl","rb"))


# In[3]:


k_fold=sklearn.model_selection.KFold(5,shuffle=True)


# In[4]:


models=[]
relavants=[]
f1s=[]
accuracies=[]
recalls=[]
for train_idx, test_idx in k_fold.split(arrays):
    arrays_train,arrays_test=arrays[train_idx],arrays[test_idx]
    labels_train,labels_test=labels[train_idx],labels[test_idx]
    model=logistic_rg.fit(arrays_train,labels_train)
    models.append(model)
    predicted_labels=model.predict(arrays_test)
    proba=model.predict_proba(arrays_test)
    relavants.append((np.average(proba[0][0]),np.average(proba[0][1])))
    f1=sklearn.metrics.f1_score(labels_test,predicted_labels,pos_label="+1")
    accuracy=sklearn.metrics.accuracy_score(labels_test,predicted_labels)
    recall=sklearn.metrics.recall_score(labels_test,predicted_labels,pos_label="+1")
    f1s.append(f1)
    accuracies.append(accuracy)
    recalls.append(recall)


# In[5]:


f1s


# In[6]:


accuracies


# In[7]:


recalls


# In[8]:


relavants


# In[15]:


plt.scatter([i[1] for i in relavants],recalls)
plt.show


# In[16]:


plt.scatter(range(5),recalls)
plt.show

