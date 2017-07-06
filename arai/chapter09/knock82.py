import random

for line in open('knock81.txt'):
    words = line.strip().split()
    for i, word in enumerate(words):
        d = random.randint(1, 5)
        c = words[i-d:i] + words[i+1:i+d+1]
        print('{}\t{}'.format(word,(' '.join(c))))
        
