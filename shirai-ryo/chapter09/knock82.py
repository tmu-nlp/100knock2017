import random

"""
うまくいかなかったけど一応取っておこうかと思いました
思いました
思いました

with open('corpus81.txt') as in_text:
    t = []
    for line in in_text:
        words = line.split()
        for i in range(len(words)):
            if len(words[i]) > 0:
                t.append(words[i])
    # tに単語で区切って全部入れたなう

for i in range(len(t)):
    front_c = t[i-d: i]
    back_c = t[i+1: i+d+1]
    c = "{}:{}".format(front_c, back_c)
    print("{}\t{}".format(t[i], c))

"""

"""
スライスを使う
i-dと、i+dで文脈c
dは上でやってるのでおk


"""


with open('corpus81.txt') as in_text, open('corpus82.txt', 'w') as out_text:
    for line in in_text:
        words = line.split()
        for i in range(len(words)):
            d = random.randint(1,5)
            if i - d < 0:
                start = 0
            else: # i - d > 0:
                start = i - d
            if i + d > len(words):
                end = len(words)
            else: # i + d <= len(words):
                end = i + d
            for j in range(start, end):
                if j != i:
                    #print(words[i])
                    #print(words[j])
                    out_text.write("{}\t{}\n".format(words[i], words[j]))
