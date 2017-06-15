import re

def sentence_segmentation(line):
        seg_list = []
#    for line in  text :
#        seg_list = []
        sentence = re.findall(r'([A-Z].*?[\.;:\?]\s)', line)
        if sentence:
            seg_list = sentence
            #print(sentence)
        return seg_list
            
if __name__ == '__main__':
    with open('nlp.txt') as text:
        for line in text:
            sentence_list = sentence_segmentation(line)
            if sentence_list:
                for sentence in sentence_list:
                    print(sentence, end = '\n')



