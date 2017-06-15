import nltk
import re

stemmer = nltk.PorterStemmer()
with open('answer51.txt','r') as i_f,open('answer52.txt','w') as a_f:
    for words in i_f:
        pattern = r',|:|\.|\(|\)|\'|\"'
        word = re.sub(pattern,'',words)
        word = word.split('\n')
        for i in range(len(word)):
            ans = stemmer.stem(word[i])
            a_f.write(word[i] + '\t\t' + ans + '\n')
