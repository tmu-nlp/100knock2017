import numpy as np

input = "I couldn't believe that I could actually understand \
what I was reading : the phenomenal power of the human mind ."
print(input.split(' '))

def shuffle(str):
    shuffledStr = ''.join(np.random.permutation(np.array(list(str[1:-1]))).tolist())
    return str[0] + shuffledStr + str[-1]

print([w if len(w) <= 4 else shuffle(w) for w in input.split(' ')])