
# coding: utf-8

# In[6]:

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys, pprint, re


# In[63]:

sec=re.compile("\{\{基礎情報 国.+?\n\}\}\n",flags=re.DOTALL)
key_value=re.compile("\n\|(.+?) = (.+?)\n\|",flags=re.DOTALL)


# In[44]:

with open("./UK.txt","r") as f:
    lines=f.read()


# In[71]:

match=sec.findall(lines)
dict_items=key_value.findall(match[0])
dict={i:j for i, j in dict_items}
pprint.pprint(dict)



# In[ ]:



