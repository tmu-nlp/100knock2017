'''
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語ttに関して，単語ttと文脈語ccのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

ある単語ttの前後dd単語を文脈語ccとして抽出する（ただし，文脈語に単語ttそのものは含まない）
単語ttを選ぶ度に，文脈幅ddは{1,2,3,4,5}{1,2,3,4,5}の範囲でランダムに決める．
----------------------------------------------------------------------------------

83. 単語／文脈の頻度の計測

82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数

'''

import random
from collections import defaultdict
import dill
import sys

f_t_c = defaultdict(lambda: 0)
f_t_star = defaultdict(lambda: 0)
f_star_c = defaultdict(lambda: 0)

with open('undersore.txt') as f:
    for n, line in enumerate(f):
        # print('{} '.format(\rint(n)/284434))
        sys.stdout.write("\r%d/284434" % n)
        words = line.lower().strip().split()
        for idx, t in enumerate(words):
            f_t_star[t] += 1
            l = len(words)
            d_max = 5
            if l <= d_max:
                d_max = l-1

            #単語tの位置idxが5未満、もしくはラスト４単語に入っていれば、dの最大値を減らす
            if idx < d_max:
                d_max = idx
            elif idx >= l-d_max:
                d_max = l - idx - 1

            if d_max > 1:
                d = random.randint(1, d_max)
                ctxs = words[idx-d_max:idx] + words[idx+1:idx+d_max+1]
                for ctx in ctxs:
                    # print('{}\t{}'.format(t,ctx)) # knock82
                    f_t_c[t + '|_' + ctx] += 1
                    f_star_c[ctx]  += 1
                #print('{}\t{}, {}'.format(t, ''.join(words[idx-d_max:idx]), ''.join(words[idx+1:idx+d_max+1])))
            else:
                pass


# knock 83
with open("f_dist.dill", "wb") as f:
    dill.dump((f_t_c, f_t_star, f_star_c), f)