import random

all_sentence = list()
with open('rt-polaritydata/rt-polaritydata/rt-polarity.neg', encoding='latin-1') as f_n:
    for line in f_n:
        line1 = '-1 ' + line
        all_sentence.append(line1)

with open('rt-polaritydata/rt-polaritydata/rt-polarity.pos', encoding='latin-1') as f_p:
    for line in f_p:
        line2 = '+1 ' + line
        all_sentence.append(line2)
random.shuffle(all_sentence)

with open('sentiment.txt', 'w') as output_f:
    for line in all_sentence:
        output_f.write(line)
