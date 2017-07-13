from gensim.models import word2vec
import sys

if __name__ == '__main__':
#    保存のお話
#    sentences = word2vec.LineSentence(sys.argv[1])
#    model = word2vec.Word2Vec(sentences, sg = 1, size = 100, min_count = 1, window = 10, hs = 1, negative = 0)
#    model.save(sys.argv[2])
#   呼び出しのお話
    model = word2vec.Word2Vec.load('model.w2v')
    print('knock86')
    print(model['United_States'])
    print('knock87')
    print(model.similarity('United_States', 'US'))
    print('knock88')
    for line in model.most_similar(positive = ['England']):
        print(line[0], line[1])
    print('knock89')
    for line in model.most_similar(positive = ['Spain', 'Athens'], negative = ['Madrid']):
        print(line[0], line[1])
