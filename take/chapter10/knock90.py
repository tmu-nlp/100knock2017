'''
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
'''


import word2vec
import os
import sys
from pprint import pprint

def generate_model(_size=150):
    # model_file = 'model90.bin'
    word2vec.word2vec('undersore.txt', model_file, size=_size, min_count=10, verbose=True)
    print('Model generated: ' + model_file)

def load_model():
    return word2vec.load('model90.bin')

def solve_87to89_by_w2v():

    # United_Statesのベクトル # knock 86
    print('--- knock86: United_States のベクトル---\n')
    pprint(model['United_States'])

    # knock 87
    print('\n--- knock87: United_States とコサイン類似度が高い上位10件. ---\n')
    #戻りはタプルで、indexesにはヴォきゃ内の類似単語のid、metrixsには対応するコサイン類似度
    indexes, metrics = model.cosine('United_States')
    pprint(model.generate_response(indexes, metrics).tolist())

    # knock 88
    print('\n--- knock88: England とコサイン類似度が高い上位10件. ---\n')
    #戻りはタプルで、indexesにはヴォきゃ内の類似単語のid、metrixsには対応するコサイン類似度
    indexes, metrics = model.cosine('England')
    pprint(model.generate_response(indexes, metrics).tolist())

    # knock89
    print('\n--- knock89: Spain - Madrid + Athens と類似度が高い上位10件. ---\n')
    indexes, metrics = model.analogy(pos=['Spain', 'Athens'], neg=['Madrid'], n=10)
    pprint(model.generate_response(indexes, metrics).tolist())



if __name__ == '__main__':
    model_file = 'model90.bin'
    if not os.path.exists(model_file):
        generate_model()
    
    # try:
    #     model = load_model()
    # except:
    #     sys.exit(1)
        
    model = word2vec.load('model90.bin')

    print('w2v model shape: {}'.format(model.vectors.shape))

    solve_87to89_by_w2v()

    #indexから単語を引く
    # model.vocab[indexes]

    # # United_Statesのベクトル # knock 86
    # print('--- knock86: United_States のベクトル---\n')
    # pprint(model['United_States'])
    #
    # # knock 87
    # print('\n--- knock87: United_States とコサイン類似度が高い上位10件. ---\n')
    # #戻りはタプルで、indexesにはヴォきゃ内の類似単語のid、metrixsには対応するコサイン類似度
    # indexes, metrics = model.cosine('United_States')
    # pprint(model.generate_response(indexes, metrics).tolist())
    #
    # # knock 88
    # print('\n--- knock88: England とコサイン類似度が高い上位10件. ---\n')
    # #戻りはタプルで、indexesにはヴォきゃ内の類似単語のid、metrixsには対応するコサイン類似度
    # indexes, metrics = model.cosine('England')
    # pprint(model.generate_response(indexes, metrics).tolist())
    #
    # # knock89
    # print('\n--- knock89: Spain - Madrid + Athens と類似度が高い上位10件. ---\n')
    # indexes, metrics = model.analogy(pos=['Spain', 'Athens'], neg=['Madrid'], n=10)
    # pprint(model.generate_response(indexes, metrics).tolist())
    #
