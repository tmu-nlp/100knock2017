# 軽い方のファイルでやっておkっぽい
# knock84はもっと増やす
# knock85は次元数を減らす

import re

with open("enwiki-20150112-400-r100-10576.txt", "r") as in_text, open("corpus80.txt", "w") as out_text:
    for line in in_text:
        words = line.split()
        new_words = []
        for word in words:
            word = re.sub('^[\.\,\!\?\;\:\(\)\[\]\'\"]|[\.\,\!\?\;\:\(\)\[\]\'\"]$', "", word)
            # 行頭と行末のやつを置き換えてる
            if len(word) != 0:
                new_words.append(word)
        out_text.write(' '.join(new_words) + '\n')
