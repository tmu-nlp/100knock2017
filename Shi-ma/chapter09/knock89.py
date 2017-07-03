from knock87 import *


if __name__ == '__main__':
    with open('result/knosk83_result.dump', 'rb') as data_in:
        ids_t = pickle.load(data_in)[1]

    X_100 = io.loadmat('result/knock85_result.mat')['X_100']

    vec_target = X_100[ids_t['Spain']] - X_100[ids_t['Madrid']] + X_100[ids_t['Athens']]
    word_simi_list = list()

    for i in range(len(X_100)):
        word_simi_list.append((i, calc_cos_simi(vec_target, X_100[i])))

    sorted_ids_t = sorted(ids_t.items(), key=lambda x: x[1])
    for word_simi in sorted(word_simi_list, key=lambda x: x[1], reverse=True)[:10]:
        print('{}\t{}'.format(sorted_ids_t[word_simi[0]][0], word_simi[1]))
