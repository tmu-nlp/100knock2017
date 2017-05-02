from knock05 import ngram

X = set(ngram('paraparaparadise', 2))
Y = set(ngram('paragraph', 2))

print('X | Y\t' + str(X | Y))
print('X & Y\t' + str(X & Y))
print('X - Y\t' + str(X - Y))
print('Y - X\t' + str(Y - X))

print("'se' in the X?: ", ('s', 'e') in X)
print("'se' in the Y?: ", ('s', 'e') in Y)
