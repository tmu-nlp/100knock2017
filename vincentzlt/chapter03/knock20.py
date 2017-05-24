
# coding: utf-8

# In[15]:

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys,gzip,json,pprint


# In[11]:

json_list=[]
for line in gzip.open("./jawiki-country.json.gz","rt"):
    json_list.append(json.loads(line))
    


# In[19]:

with open("UK.txt","w",encoding="UTF-8") as f:
    for i in json_list:
        if i["title"]=="イギリス":
            f.write(i["text"])


# In[ ]:



