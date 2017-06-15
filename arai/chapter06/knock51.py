from knock50 import sentence_segmentation
import re

with open('nlp.txt') as text:
    for line in text:
        sentence_list = sentence_segmentation(line)
        for sentence in sentence_list:
            word = sentence.split()        #print(sentence)
            print('\n'.join(word))
            print('\n')
