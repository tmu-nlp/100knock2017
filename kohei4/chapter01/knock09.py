import random

#### PreCheck Code
#test=list("abcdefg")
#print(test)
#random.shuffle(test)
#print(test)
#a = ''.join(test)
#print(a)
#####################

tgt= "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

l_tgt = tgt.split()

ns = ""

for i in range(len(l_tgt)):
    if len(l_tgt[i]) > 4:
        t = l_tgt[i][0]
        l = l_tgt[i][-1]
        mw = list(l_tgt[i][1:-1])
        random.shuffle(mw)
#        print(mw)
        nw = t + "".join(mw) + l
    else:
        nw = l_tgt[i]
    
    if i == len(l_tgt) -1:        
        ns = ns + nw
    else:
        ns = ns + nw + " "
    
print(ns)