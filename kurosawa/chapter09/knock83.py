from collections import defaultdict
import pickle

if __name__ == '__main__':
    list_file = 't_c_list.txt'
    with open(list_file) as list_data:
        N = 0
        f = defaultdict(int)
        for i,line in enumerate(list_data):
            t,c = line.strip().split('\t')
#            c_list = c_list.split()
            f[t+' | *'] += 1
#            for c in c_list:
            N += 1
            f[t+' | '+c] += 1
            f['* | '+c] += 1
            if i%1000000 == 0:
                print(i)
    with open('83_N','wb') as n_data, open('83_f','wb') as f_data:
        pickle.dump(N,n_data)
        pickle.dump(f,f_data)
