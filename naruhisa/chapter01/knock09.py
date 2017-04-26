import random

s = "I couldn't believe that I could actually understand what was reading : the phenomenal power of the human mind ."
tmp = ''
s = s.split()

for i in range(len(s)):
    if(len(s[i]) > 4):
        tmp = s[i][1:-1]
        tmp = list(tmp)
        random.shuffle(tmp)
        tmp = ''.join(tmp)
        s[i] = s[i][0] + tmp + s[i][-1]
        tmp = ''

print(' '.join(s))
