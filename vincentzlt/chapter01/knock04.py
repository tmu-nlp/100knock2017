
# coding: utf-8

# In[18]:

sent='Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'


# In[19]:

pos=[1, 5, 6, 7, 8, 9, 15, 16, 19]


# In[20]:

pos=[i-1 for i in pos]


# In[21]:

count=0
output=[]
for _ in sent.replace(',','').replace('.','').split(' '):
    if (count in pos):
        count+=1
        output.append((_[0],count))
    else:
        count+=1
        output.append((_[0:2],count))
print(output)


# In[ ]:



