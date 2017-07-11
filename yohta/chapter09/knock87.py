import pickle
import numpy as np

with open('data/answer85','rb') as i_f:
    words,vector = pickle.load(i_f)

def cos_similarity(vec1, vec2):
    if (np.linalg.norm(vec1) * np.linalg.norm(vec2) == 0):
        return 0
    else:
        return np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

if __name__ == '__main__':
    vec1 = vector[words['United_States']]
    vec2 = vector[words['U.S']]
    print ('{}'.format(cos_similarity(vec1, vec2)))
