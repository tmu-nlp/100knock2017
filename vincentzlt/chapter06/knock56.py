
# coding: utf-8

# In[1]:

import sys,re,pdir
from stemming.porter2 import stem
from lxml import etree


# In[68]:

def co_ref(f_name):
    tree=etree.parse(f_name)
    root=tree.getroot()
    
    # generate sentences
    sentences=root.xpath("/root/document/sentences/sentence")
    sentence_strs=[]
    for sentnece in sentences:
        words=sentnece.xpath("./tokens/token")
        sentence_str=" ".join(w[0].text for w in words)
        sentence_strs.append(sentence_str)
        
    # processing co_ref
    co_refs=root.xpath("/root/document/coreference/coreference")
    for co_ref in co_refs:
        mention_repr=(None,None)
        mentions=[]
        sentence_id=None
        for mention in co_ref:
            if mention.get("representative")=="true":
                mention_repr=(int(mention[0].text),mention[4].text)
            else:
                mentions.append((int(mention[0].text),mention[4].text))
        for mention in mentions:
            sent_id=mention[0]-1 #sentence to be replaced
            old_str=mention[1]
            new_str=mention_repr[1]
            sentence_strs[sent_id]=sentence_strs[sent_id].replace(old_str,new_str)
            print(sentence_strs[sent_id])
        
       


# In[69]:

if __name__=="__main__":
    xml_path="./nlp_sentence_break.txt.xml"
    co_ref(xml_path)


# In[ ]:



