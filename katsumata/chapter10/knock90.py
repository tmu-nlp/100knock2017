from gensim.models import word2vec
import logging
import sys

def make_emb(file_name):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus('tokens_knock81.txt')
    model = word2vec.Word2Vec(sentences, size=300, min_count=10, window=3)
    model.save('knock90.emb')
    return model

def load_emb():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model=word2vec.Word2Vec.load('knock90.emb')
    return model
    

if __name__ == '__main__':
    file_name = 'tokens_knock81.txt' 
    make_load = input('Make?Load? ')
    if make_load == 'Make':
        model=make_emb(file_name)
    elif make_load == 'Load':
        model=load_emb()
    
    print ('knock86 "United States"')
    print (model['United_States'])
    print ()
    print ('knock87 sim "US"')
    print (model.similarity('United_States', 'U.S'))
    print ()
    print ('knock88 England Top 10')
    for x in model.most_similar(positive=['England']):
        print (x[0], x[1])
    print ()
    print ('knock89 analogy')
    for x in model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid']):
        print (x[0], x[1])
