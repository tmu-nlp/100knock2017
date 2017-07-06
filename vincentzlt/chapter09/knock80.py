
# coding: utf-8

# In[9]:


import time,re,time


# In[2]:


f_name="./enwiki-20150112-400-r10-105752.txt"


# In[4]:


text=open(f_name,"r",encoding="utf-8").readlines()


# In[18]:


text_=[]
st=time.time()
for idx, line in enumerate(text):
    
    if idx%100000==0:
        print("processed {} sentence in {} second.".format(idx,time.time()-st))
        st=time.time()
    line_=[]
    for w in line.split():
        w=w.strip(".,!?;:()[]\'\" ")
        line_.append(w)
    text_.append(" ".join(line_)+"\n")


# In[19]:


with open(f_name+".token","w",encoding="utf-8") as f_out:
    f_out.writelines(text_)

