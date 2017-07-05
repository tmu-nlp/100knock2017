import codecs
import random

pos_file = 'rt-polaritydata/rt-polarity.pos'
neg_file = 'rt-polaritydata/rt-polarity.neg'
concat_file = 'sentiment.txt'

with codecs.open(pos_file,'r','cp1252') as pos_f,codecs.open(neg_file,'r','cp1252') as neg_f:
    concat_sentence = []
    pos_counter = 0
    neg_counter = 0

    for line in pos_f:
        line.strip()
        line = '+1 ' + line
        concat_sentence.append(line)
        pos_counter += 1
    print('pos:{}'.format(pos_counter))

    for i,line in enumerate(neg_f):
        line.strip()
        line = '-1 ' + line
        concat_sentence.append(line)
        neg_counter += 1
    print('neg:{}'.format(neg_counter))

    random.shuffle(concat_sentence)
#    print(len(concat_sentence))

with open(concat_file,'w') as con_f:
    for i in range(len(concat_sentence)):
        con_f.write(concat_sentence[i])
