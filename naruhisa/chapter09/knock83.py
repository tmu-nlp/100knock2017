from collections import defaultdict
import pickle

if __name__ == '__main__':
    co_occur = defaultdict(lambda: 0)
    count_word = defaultdict(lambda: 0)
    count_context = defaultdict(lambda: 0)
    with open('tokens82.txt', 'r') as i_f:
        for i, line in enumerate(i_f):
            t, c = line.split('\t')
            c = c.split()
            for c_s in c:
                co_occur[t + '\t' + c_s] += 1
                count_word[c_s] += 1
            count_context[t] += 1
        N = i + 1
    print(N)
    with open('f.dumps', 'wb') as fb:
        pickle.dump((dict(co_occur), dict(count_word), dict(count_context), N), fb)
