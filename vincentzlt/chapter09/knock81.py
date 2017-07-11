
# coding: utf-8

# In[1]:


import time,re,time


# In[5]:


f_name="./enwiki-20150112-400-r10-105752.txt.token"
f_c_name="./country_names_with_space"


# In[6]:


text=open(f_name,"r",encoding="utf-8").readlines()
c_names=open(f_c_name,"r",encoding="utf-8").readlines()


# In[7]:



def r_c_name(c_name):
    return "_".join(c_name.split())


# In[11]:



st=time.time()
for idx in range(len(text)):
    
    if idx%100000==0:
        print("processed {} sentence in {} second.".format(idx,time.time()-st))
        st=time.time()
    for c_name in c_names:
        text[idx]=text[idx].replace(c_name,r_c_name(c_name))


# In[12]:


with open(f_name+".contry_name","w",encoding="utf-8") as f_out:
    f_out.writelines(text)

