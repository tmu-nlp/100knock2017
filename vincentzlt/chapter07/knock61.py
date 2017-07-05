
# coding: utf-8

# In[29]:


import redis,json,gzip
from pprint import pprint




r=redis.StrictRedis(host="127.0.0.1",port=6379,db=0)




def search_loc(band_name):
    return r.hget(name="area",key=band_name)


# In[47]:


print(search_loc("Oasis"))


# In[ ]:




