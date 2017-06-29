# -*- coding: utf-8 -
import random

sentiment = []

for line in open('rt-polaritydata/rt-polaritydata/rt-polarity.pos', 'rb'):
    sentiment.append('+1' + '\t' + line.decode('latin-1'))

for line in open('rt-polaritydata/rt-polaritydata/rt-polarity.neg', 'rb'):
    sentiment.append('-1' + '\t' + line.decode('latin-1'))

random.shuffle(sentiment)

text = open('sentiment.txt' , 'w')
for line in sentiment:
    text.write(line)

    


