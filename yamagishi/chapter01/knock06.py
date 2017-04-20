from knock05 import ngram

X = set(ngram('paraparaparadise', 2))
Y = set(ngram('paragraph', 2))

print('X | Y\t' + str(X | Y))
print('X & Y\t' + str(X & Y))
print('X - Y\t' + str(X - Y))
