from collections import defaultdict
import pickle

if __name__ == '__main__':
    co_occur_dict = defaultdict(int)
    count_word = defaultdict(int)
    count_context = defaultdict(int)
    with open('context_knock82.txt') as i_f:
        count_pair=0
        for line in i_f:
            co_occur_dict[line.strip()]+=1
            count_word[line.strip().split('\t')[0]]+=1
            count_context[line.strip().split('\t')[1]]+=1 
            count_pair+=1
    with open('word_context_freq.dump','wb') as o_f:
        pickle.dump((dict(co_occur_dict),dict(count_word),dict(count_context),count_pair), o_f)
