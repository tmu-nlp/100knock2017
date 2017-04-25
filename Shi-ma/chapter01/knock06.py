def ngram_l(n, txt):
    words_l = list(map(str, txt.replace(',', ' ').replace('.', ' ').split()))
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
txt_X = 'paraparaparadise'
txt_Y = 'paragraph'
n = 2
X = set(ngram_l(n, txt_X)[0])
Y = set(ngram_l(n, txt_Y)[0])

print('X & Y :', list(X & Y))
print('X | Y :', list(X | Y))
print('X - Y :', list(X - Y))

if 'se' in X:
    print('"se"がXに含まれる')
else:
    print('"se"がXに含まれない')
if 'se' in Y:
    print('"se"がYに含まれる')
else:
    print('"se"がYに含まれない')
