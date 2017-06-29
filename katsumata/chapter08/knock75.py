import pickle

with open('weight.dump', 'rb') as w_f:
    w = pickle.load(w_f)
print ('重みの高い素性トップ10')
i = 0
for key, value in sorted(w.items(), key=lambda x:x[1], reverse=True):
    print ('{}: {}\t{}'.format(i+1, key, value))
    i += 1
    if i == 10:
        break
print()
print ('重みの低い素性トップ10')
i=0
for key, value in sorted(w.items(), key=lambda x:x[1]):
   print ('{}: {}\t{}'.format(i+1, key, value))
   i += 1
   if i == 10:
       break
   
