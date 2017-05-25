import knock30
import collections

if __name__ == '__main__':
    with open('../data/neko.txt.mecab', 'r') as data_in:
        mecab_data = knock30.mecab_dict_data(data_in)
        rank_word = collections.defaultdict(lambda: 0)
        for line in mecab_data:
            for word in line:
                rank_word[word['surface']] += 1
    rank_word = sorted(rank_word.items(), key=lambda x: x[1], reverse=1)
    with open('../data/neko_word_rank.txt', 'w') as data_out:
        for word in rank_word:
            data_out.write(str(word) + '\n')
