
# coding: utf-8

# In[19]:


import re


# In[23]:


lines=[]
flag=False
for line in open("./questions-words.txt","r",encoding="utf-8"):
    if line.startswith(": family"):
        flag=True
    elif line.startswith(": "):
        flag=False
    
    if flag:
        lines.append(line)


# In[25]:


with open("family.txt","w",encoding="utf-8") as f:
    f.writelines(lines)

