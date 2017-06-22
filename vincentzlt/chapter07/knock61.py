
# coding: utf-8

# In[29]:


import redis,json,gzip
from pprint import pprint


# In[30]:


m_jsons=[]


# In[31]:


r=redis.StrictRedis(host="127.0.0.1",port=6379,db=0)


# In[32]:


for line in open("./artist.json", "r", encoding="utf-8"):

    m_jsons.append(json.loads(line))


# In[39]:


for rc in m_jsons:
    if 'area' in rc:
        r.hset(key=rc["name"],name="area",value=rc['area'])


# In[46]:


def search_loc(band_name):
    return r.hget(name="area",key=band_name)


# In[47]:


search_loc("Oasis")


# In[ ]:




