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

x = []
y = []
for i, (key, value) in enumerate(rank_word):
    x.append(i+1)
    y.append(value)
plt.plot(x, y)
plt.xscale('log')
plt.yscale('log')
plt.savefig('knock39_result.png')
