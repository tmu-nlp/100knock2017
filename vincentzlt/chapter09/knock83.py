
# coding: utf-8

# In[7]:


import time,re,time,random
from collections import Counter
import pickle


# In[2]:


f_name="./enwiki-20150112-400-r10-105752.txt.token.contry_name.contexts"


# In[3]:


text=open(f_name,"r",encoding="utf-8").readlines()


# In[ ]:


for idx in range(len(text)):
    t_c=text[idx].split("\t")
    text[idx]=(t_c[0],t_c[1])


# In[ ]:


f_tc=Counter(text)
f_t=Counter([tc[0] for tc in text])
f_c=Counter([tc[1] for tc in text])
N=len(text)


# In[ ]:


with open(f_name+".counter.pkl","wb") as f_out:
    pickle.dump((f_tc,f_t,f_c,N),f_out)

