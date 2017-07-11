
# coding: utf-8

# In[3]:


import time,re,time,random,math

from collections import Counter
import pickle


# In[2]:


f_name="./enwiki-20150112-400-r10-105752.txt.token.contry_name.contexts"


# In[3]:


f_tc,f_t,f_c,N=pickle.load(file=open(f_name,"rb"))


# In[ ]:


ppmis=[]
for tc in f_tc:
    if f_tc[tc]>10:
        ppmi=max(math.log((N*f_tc[tc])/((f_t[tc[0]])*(f_c[tc[1]]))),0)
    ppmis.append(ppmi)


# In[ ]:


with open(f_name+".ppmis","wb") as f_out:
    pickle.dump((ppmis),f_out)

