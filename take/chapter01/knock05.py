def make_ngram(seq, mode='c', n=2, delim=''):
    if mode == 'c': #char-based
        targetSeqList = list(seq)
    elif mode == 'w': #word-based
        targetSeqList = seq.split()
    else:
        print('mode引数まちごうとるでー')
        exit(1)

    result = [] # 最終的にsetへ変更するなら最初からsetでいいけど、\
                # 文字列を分割したときの経緯を明示的に残すために、一旦リストをつかう

    for i, w in enumerate(targetSeqList):
        # if i == len(targetSeqList)-(n-1): #n-gramの構成終了判定。部分リストngramListの生成コストが不要だがわかりづらい
        #     break
        ngramList = targetSeqList[i:i+n]
        # print(ngramList) #sanity check
        # print(len(ngramList))
        if len(ngramList) < n: #n-gram構成終了判定。部分リストngramListの生成しないといけないが、わかりやすい
            break
        if ngramList[-1] == '.':
            break
        # result.append(w + delimiter + targetSeqList[i+1])
        result.append(delim.join(ngramList))

    return result

if __name__ == '__main__':
    print('word-based: ', make_ngram("I am an NLPer .", mode='w', n=4, delim='-'))
    print('char-based: ', make_ngram("I am an NLPer .", mode='c', n=4))
