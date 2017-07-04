from gensim.models import word2vec
from scipy import io
import numpy as np
import pickle


if __name__ == '__main__':
    X_100_85 = io.loadmat('../chapter09/result/knock85_result.mat')['X_100']
    X100_90 = word2vec.Word2Vec.load('result/knock90_result/model.bin')

    with open('../chapter09/result/knock83_result.dump', 'rb') as data_in:
        ids_t = pickle.load(data_in)[1]

    with open('result/knock91_result.txt', 'r') as data_in:
        with open('result/knock92_85_result.txt', 'w') as data_out_85, open('result/knock92_90_result.txt', 'w') as data_out_90:
            sorted_ids_t = sorted(ids_t.items(), key=lambda x: x[1])

            for line in data_in:
                cols = line.strip().split()
                if not all(map(lambda x: x in ids_t.keys(), cols)) or not all(map(lambda x: x in X100_90, cols)):
                    continue
                vec_85 = X_100_85[ids_t[cols[1]]] - X_100_85[ids_t[cols[0]]] + X_100_85[ids_t[cols[2]]]
                max_index_simi_85 = (0, 0)
                for i in range(len(X_100_85)):
                    if np.dot(vec_85, X_100_85[i]) > max_index_simi_85[1]:
                        max_index_simi_85 = (i, np.dot(vec_85, X_100_85[i]))
                print(line.strip() + ' {} {}'.format(sorted_ids_t[max_index_simi_85[0]][0], max_index_simi_85[1]), file=data_out_85)

                max_word_simi_90 = X100_90.most_similar(positive=[cols[1], cols[2]], negative=[cols[0]], topn=1)[0]
                print(line.strip() + ' {} {}'.format(max_word_simi_90[0], max_word_simi_90[1]), file=data_out_90)
