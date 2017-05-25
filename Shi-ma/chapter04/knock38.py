import knock30
import collections
import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('../data/neko.txt.mecab', 'r') as data_in:
        mecab_data = knock30.mecab_dict_data(data_in)
        rank_word = collections.defaultdict(lambda: 0)
        for line in mecab_data:
            for word in line:
                rank_word[word['surface']] += 1

    x = []
    for key, value in rank_word.items():
        x.append(value)
    plt.hist(x, bins = 200, log = 1)
    plt.savefig('knock38_result.png')
