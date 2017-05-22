
# coding: utf-8

# In[1]:

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys, pprint, re


# In[13]:

cat_all_re=re.compile("^.+?Category:.+?$")


# In[15]:

for line in open("./UK.txt","r"):
    match=cat_all_re.match(line)
    if match:
        print(match.string)


# In[ ]:



