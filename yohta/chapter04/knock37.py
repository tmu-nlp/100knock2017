#import numpy as np
import matplotlib.pyplot as plt
from knock30 import map_make
from knock30 import list_make
from collections import defaultdict

#import matplotlib.font_manager
#FP = matplotlib.font_manager.FontProperties(fname="../data/ipag.ttf")

with open('../data/neko.txt.mecab','r') as f:
    sent_list = list_make(f)
    word_list = []
    word_list_counter = defaultdict(lambda: 0)
    for i in range(0,len(sent_list)):
        for j in range(0,len(sent_list[i])):
            word_list_counter[sent_list[i][j]['surface']] += 1
    word_rank = sorted(word_list_counter.items(), key = lambda x:x[1],reverse = True)
#        print('{}:{}'.format(w,c))

    counter = 0
    words = []
    number = []
    left = []

    for word,num in word_rank:
        if counter == 10:
            break
        words.append(word)
        number.append(num)
        left.append(counter)
        counter += 1
"""
words = 該当の単語（リスト:多い順）
number = 該当単語の出現回数（リスト:多い順）
left = 横軸用の数値（リスト）
"""
#cprint(words)
plt.bar(left,number,align = 'center')
plt.xticks(left,words)
plt.show()
