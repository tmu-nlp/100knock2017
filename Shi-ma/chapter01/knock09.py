import random

txt = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = list(map(str, txt.split()))
txt_cip = []

for word in words:
    if len(word) > 4:
        temp_l = word[0]
        temp_e = word[len(word)-1]
        temp = list(word[1:len(word)-1])
        random.shuffle(temp)
        txt_cip.append(temp_l + ''.join(temp) + temp_e)
    else:
        txt_cip.append(word)

print(' '.join(txt_cip))
