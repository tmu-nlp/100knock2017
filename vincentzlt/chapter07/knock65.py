
# coding: utf-8

# In[64]:


import redis,json,gzip
from pprint import pprint
from pymongo import MongoClient


# In[65]:


Client=MongoClient()
db=Client.artist_info
collection=db.artist_info


# In[76]:


collection.drop()


# In[70]:


for idx,line in enumerate(open("./artist.json","r",encoding="utf-8")):
    j=json.loads(line)
    if "aliases" in j:
        j["aliases_name"]=[]
        for a in j["aliases"]:
            j["aliases_name"].append(a["name"])
    if "tags" in j:
        j["tags_value"]=[]
        for a in j["tags"]:
            j["tags_value"].append(a["value"])
    if "rating" in j:
        j["rating_value"]=[]
        for a in [j["rating"]]:
            j["rating_value"].append(a["value"])
    collection.insert_one(j)


# In[75]:


for f in collection.find({"name": "Queen"}):
    pprint(f)


# In[ ]:




