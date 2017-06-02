import re

with open("nlp.txt") as f:
    sentence = f.read().replace('\n', '')
#print(sentence)

# m = re.findall(r'\s(.*?[.;:?!])\s[A-Z]', sentence, re.M)
m = re.sub(r'([^.;:?!]*?[.;:?!])\s([A-Z])', r'\1\n\2' , sentence)
print(m)
# for x in m:
#     print(x) # sol 50
