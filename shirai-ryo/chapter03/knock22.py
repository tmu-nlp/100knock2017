from knock20 import wiki_UK
import re


for line in wiki_UK().split('\n'):
    cate = re.findall(r'\[\[Category:(.*?)\|*\**\]\]', line)
    #抜き出したい部分に()をしている。ここでは(.*?)
    #(.*)だと、抜き出しは一番長いのをとる
    #(.*?)だと、抜き出し一番短いのをとる
    #findall()は、文字列の中のパターンとマッチする部分をすべてリストとして返す
    if cate:
        for m in cate:
            print(cate)


# for line in wiki_UK().split('\n'):
#     if "Category:" in line:
#         cate = line.lstrip("[[Category:").rstrip("]]")
#         #strip()は文字列の先頭と末尾から削除
#         #lstrip()は文字列の先頭から削除
#         #rstrip()は文字列の末尾から削除
#
#         #strip()で問題なくできた
#
#         print(cate)
