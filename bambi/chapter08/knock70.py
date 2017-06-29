import random
'''
  Specifically: 
  * rt-polarity.pos contains 5331 positive snippets
  * rt-polarity.neg contains 5331 negative snippets
'''
pos = []
neg = []
def read_file(path, weight): 
    for line in open(path, encoding='ISO-8859-1'): # utf-8 cannot decode byte something?? so, need to add encoding
        yield "{}\t{}".format(weight,line)
for item in read_file("rt-polarity.neg","-1"):
    neg.append(item)
for item in read_file("rt-polarity.pos","1"):
    pos.append(item)
result = pos + neg
random.shuffle(result)
print("pos:{},neg:{}".format(len(pos),len(neg)))
with open("sentiment.txt","w") as output:
    output.write("".join(result))
    print("".join(result))
