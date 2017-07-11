import random

with open('tokens81.txt', 'r') as i_f, open('tokens82.txt', 'w') as o_f:
    for line in i_f:
        words = line.split()
        for i in range(len(words)):
            d = random.randint(1, 5)
            if i - d < 0:
                start = 0
            else:
                start = i - d
            if  i + d > len(words):
                end = len(words)
            else:
                end = i + d
            t = words[i]
            if i == len(words):
                c = words[start : i]
            else:
                c = words[start : i] + words[i + 1 : end]
            print('{}\t{}'.format(t, c))
            o_f.write('{}\t{}\n'.format(t, ' '.join(c)))
