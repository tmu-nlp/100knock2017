
# coding: utf-8

# In[9]:


import time,re,time,random


# In[10]:


f_name="./enwiki-20150112-400-r10-105752.txt.token.contry_name"


# In[11]:


text=open(f_name,"r",encoding="utf-8").readlines()


# In[12]:


def gen_context(line):
    output=[]
    line_=line.split()
    for idx,w in enumerate(line_):
        word=w
        context_range=random.randint(1,5)
        context=line_[idx-context_range-1:idx]+line_[idx+1:idx+2+context_range]
        for con in context:
            output.append("{}\t{}".format(word,con))
    return output


# In[ ]:


contexts=[]
st=time.time()
with open(f_name+".contexts","w",encoding="utf-8") as f_out:
    pass
for idx in range(len(text)):
    
    if idx%100000==0:
        
        with open(f_name+".contexts","a",encoding="utf-8") as f_out:
            f_out.writelines(contexts)
        contexts=[]
        
        print("processed {} sentence in {} second.".format(idx,time.time()-st))
        st=time.time()
    contexts+=gen_context(text[idx])


# In[ ]:




