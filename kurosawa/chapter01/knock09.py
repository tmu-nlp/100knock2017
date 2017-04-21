import random

def typoglycemia(strin):
    ll = len(strin)
    strout = ""
    if ll > 4:
        strout += strin[0]
        rand = random.sample(range(1,ll-1),ll-2)
        for i in rand:
            strout += strin[i]
        strout += strin[ll-1]
    else:
        strout += strin
    return strout

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
list = str.split()
l = len(list)
for i in range(l):
    print(typoglycemia(list[i]),end=" ")
print()
            
