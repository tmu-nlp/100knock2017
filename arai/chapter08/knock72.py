from knock71 import stopwords
from nltk.stem import PorterStemmer
from collections import defaultdict

#def feature(sentence):
with open('sentiment.txt') as text:
    counts = defaultdict(int)
    total_count = 0
    features = []
    stemmer = PorterStemmer()
    for line in text:
        word = line.strip().split()
        word.pop(0)
        for uni_word in word:
            stem_word = stemmer.stem(uni_word)
            #print(stem_word)
            if stopwords(stem_word) == False:
                features.append(stem_word)
                counts[stem_word] += 1
                total_count += 1
with open('knock72_file.txt', 'w') as r_text:
    for word, count in counts.items():
        r_text.write(word + '\t' + str(count) + '\n')



                #features.append(count[stem_word])
             #   print(features)
#    return features
'''
if __name__ == '__main__':
        for word in feature(text):
            print(word)
    
                #features.append(stem_word)
#print(features)
   ''' 
    
