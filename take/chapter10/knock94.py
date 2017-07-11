'''
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，
1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を
追加するプログラムを作成せよ．このプログラムを85で作成した単
語ベクトル，90で作成した単語ベクトルに対して適用せよ．
'''

from knock90 import load_model
import sys
from scipy import spatial



if __name__ == '__main__':

    try:
        model = load_model()
    except:
        print('Failed to load model')
        sys.exit(1)

    with open('./ws/combined.tab') as f:
        for l in f:
            line = l.strip().split()
            try:
                _a = model[line[0]]
                _b = model[line[1]]
                cossim = 1. - spatial.distance.cosine(_a, _b)
                print('{}\t{}'.format('\t'.join(line) ,cossim))
            except KeyError:
                print('{}\t{}'.format('\t'.join(line) ,'N/A'))
                
    #         true_of_false.append(line[3]==line[4])
    #         if line[4] == 'none':
    #             none_cnt += 1
    #
    # corr = true_of_false.count(True)
    # incor = true_of_false.count(False)
    #
    # print('all:{}\ncorr:{}\nincorr:{}\nnone:{}'.format(len(true_of_false), corr, incor, none_cnt))
