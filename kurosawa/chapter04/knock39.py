from knock30 import make_list
from collections import defaultdict
import sys
import matplotlib.pyplot as plot

def check_freq(r_file_name):
        line_list = make_list(r_file_name)
        word_freq = defaultdict(int)
        for i in range(len(line_list)):
            for j in range(len(line_list[i])):
                word_freq[line_list[i][j]['surface']] += 1
        return word_freq

if __name__ == '__main__':
    freq_list = check_freq(sys.argv[1])
#    print(freq)
    word_num = []
    word_f = []
    word_name = []
    i = 1
    for word, freq in sorted(freq_list.items(), key = lambda x : x[1], reverse = True):
        word_num.append(i)
        word_f.append(freq)
        i += 1
    plot.bar(word_num, word_f, width = 0.4)
    plot.xscale('log')
    plot.yscale('log')
    plot.show()
