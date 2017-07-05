import pickle
import math
from collections import defaultdict

if __name__ == '__main__':
    N_file_name = '83_N'
    f_file_name = '83_f'
    with open(N_file_name,'rb') as N_data, open(f_file_name, 'rb') as f_data:
        N = pickle.load(N_data)
        f = pickle.load(f_data)
    X = defaultdict(dict)
    i = 0
    for word_set, num in f.items():
        if num >= 10:
            t,c = word_set.split(' | ')
            if t != '*' and c != '*':
                PPMI_tc = math.log2(N*num/f[t+' | *']/f['* | '+c])
#                print(PPMI_tc)
                if PPMI_tc > 0:
                    X[t][c] = PPMI_tc
        i += 1
        if i%1000000 == 0:
            print(i)
    with open('84_X','wb') as x_data:
        pickle.dump(X,x_data)

