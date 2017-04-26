def ngram_w(n, txt):
    words_w = txt.replace(',', ' ').replace('.', ' ').split()
    txt_ngw = []

    if len(words_w) >= n:
        for i in range(len(words_w)-n+1):
            ngw = []
            for j in range(i, i+n):
                ngw.append(words_w[j])
            txt_ngw.append(ngw)
        return txt_ngw
    else:
        return words_w

def ngram_l(n, txt):
    words_l = txt.replace(',', ' ').replace('.', ' ').split()
    txt_ngl = []

    for i in range(len(words_l)):
        if len(words_l[i]) > n:
            ngl = []
            for j in range(len(words_l[i])-n+1):
                ngl.append(words_l[i][j:j+n])
        else:
            ngl = words_l[i]
        txt_ngl.append(ngl)
    return txt_ngl

# main #
txt = 'I am an NLPer'
n = 2
txt_ngw = ngram_w(n, txt)
txt_ngl = ngram_l(n, txt)
print(txt_ngw)
print(txt_ngl)
