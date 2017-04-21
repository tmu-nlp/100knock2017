import random

def swap(word):
    if len(word) < 4:
        return word
    else:
        word = list(word)
        first = word.pop(0)
        last = word.pop(-1)
        random.shuffle(word)
        return ''.join(list(first) + word + list(last))

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

ans = list()
for word in sentence.strip().split():
    ans.append(swap(word))

print(' '.join(ans))
