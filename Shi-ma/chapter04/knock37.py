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
    rank_word = sorted(rank_word.items(), key=lambda x: x[1], reverse=1)

    bar_n = 10
    labels = []
    left = []
    width = []
    counter = 1
    for label, value in rank_word:
        if counter > bar_n:
            break
        labels.append(label)
        left.append(bar_n - counter)
        width.append(value)
        counter += 1
    plt.barh(left, width)
    plt.yticks(left, labels)
    plt.savefig('knock37_result.png')
