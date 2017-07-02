from scipy import io
import numpy as np
import math
import pickle


def calc_cos_simi(x, y):
    if np.linalg.norm(x) * np.linalg.norm(y) == 0:
        return -1
    else:
        return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))


if __name__ == '__main__':
    with open('result/knosk83_result.dump', 'rb') as data_in:
        ids_t = pickle.load(data_in)[1]

    X_100 = io.loadmat('result/knock85_result.mat')['X_100']

    vec_United = X_100[ids_t['United_States']]
    vec_US = X_100[ids_t['U.S']]

    print(calc_cos_simi(vec_United, vec_US))
