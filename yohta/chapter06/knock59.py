import xml.etree.ElementTree as et
import re

# def func59(list):
pattern = r'^\((.*?)\s(.*)\)$'
# ^\(:文字列先頭の(
# tagはnon-greedy
# valueはgreedy
# \)$:文字列最後尾の)
def func59(string,ansadd):
#    pattern = re.compile(r'^\(\t\s)
    match = re.match(pattern,string)    #re.macth = re.compile + match ?
#    match = pattern.match(string)
    tag = match.group(1)    #括弧のすぐ後ろを抽出
#    print(tag)
    value = match.group(2)  #tagの後ろが\sで、その後に\(が来ないもの
#    print(value)
    # 再帰ver
    depth = 0       # 階層の深度
    word = ''       # 単語
    words = []      # 単語のappend先
    for ch in value:    # ch:1文字毎に
#        print(c)
        if ch == '(':
            word += ch
            depth += 1      # 階層+1
        elif ch == ')':
            word += ch
            depth -= 1      # 階層-1
            if depth == 0:
                words.append(func59(word, ansadd))  # 再帰
                word = ''   # word初期化
        else:
            # 括られていない時の空白は無視
            if not (depth == 0 and ch == ' '):
                word += ch
    # 最後の単語を追加
    if word != '':
        words.append(word)
    ans = ' '.join(words)

    # NPならlist_npに追加
    if tag == 'NP':
        ansadd.append(ans)
    return ans

if __name__ =='__main__':
    with open('../data/nlp.txt.xml') as i_f,open('answer59.txt','w') as a_f:
        par = et.parse(i_f)
        for sentence in par.iterfind('./document/sentences/sentence/parse'):
            ans = []
            func59(sentence.text.strip(), ans)
            if ans[0] != '.':
                for i in range(len(ans)):
                    a_f.write('NP:\t{}\n'.format(ans[i]))
