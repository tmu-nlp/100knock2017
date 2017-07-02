from knock71 import search_stopword
import nltk

stm = nltk.PorterStemmer()
with open('sentiment.txt', 'r') as i_f, open('neo_senti.txt', 'w') as o_f:
    for line in i_f:
        tmp = list()
        text = line.split()
        tmp.append(text[0])
        del text[0]
        for word in text:
            if search_stopword(word) or len(word) < 2:
                pass
            else:
                tmp.append(stm.stem(word))
        o_f.write(' '.join(tmp) +'\n')
