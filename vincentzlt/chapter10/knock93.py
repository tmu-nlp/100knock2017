
# coding: utf-8

# In[3]:


import word2vec
from pprint import pprint


# In[4]:


model=word2vec.load("./enwiki-20150112-400-r10-105752.bin")


# In[6]:


analogies=[]
correct=[]
for line in open("./family.txt","r",encoding="utf-8"):
    if not line.startswith(": "):
        w1,w2,w3,w4=line.split()
        try:
            idx, metrics=model.analogy(pos=[w2,w3],neg=[w1],n=1)
            print("+ {} {} - {}".format(w2,w3,w1))
            word,score=model.generate_response(idx,metrics).tolist()[0]
            pprint(word)
            print()
            
            if word==w4:
                correct.append(True)
            else:
                correct.append(False)
                
        except KeyError:
            pass
        
print(sum(correct)/len(correct))

