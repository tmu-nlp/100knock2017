
# coding: utf-8

# In[6]:

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys, pprint, re


# In[82]:

sec=re.compile("\{\{基礎情報 国.+?\n\}\}\n",flags=re.DOTALL)
key_value=re.compile("^\|(.+?) = (.+?)\n(?=\|)",flags=re.DOTALL|re.MULTILINE)
inner_link=re.compile("\[\[(.+?)\]\]")


# In[44]:

with open("./UK.txt","r") as f:
    lines=f.read()


# In[79]:

match=sec.findall(lines)
dict_items=key_value.findall(match[0])
dict={i:j for i, j in dict_items}



# In[84]:

for i in dict:
    dict[i]=re.sub("\'\'|\'\'\'|\'\'\'\'","",dict[i])


for i in dict:
    simple_inner_link=inner_link.findall(dict[i])
    if simple_inner_link:
        _str="\n".join(simple_inner_link)
        dict[i]=re.sub("^[^\|]+?\|","",_str)
pprint.pprint(dict)




