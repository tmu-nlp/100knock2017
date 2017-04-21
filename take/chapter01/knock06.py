from knock05 import make_ngram

s1 = 'paraparaparadise'
s2 = 'paragraph'

X = make_ngram(s1)
Y = make_ngram(s2)

Xset = set(X)
Yset = set(Y)

union = Xset | Yset # Xset.union(Yset)
product = Xset & Yset # Xset.intersection(Yset)
diff = Xset - Yset # Xset.difference(Yset)

# 演算子の作用を確認したかっただけ
# assert union == Xset.union(Yset)
# assert product == Xset.intersection(Yset)
# assert diff == Xset.difference(Yset)

print('X:{0}\nY:{1}'.format(X,Y))
print("和:{0}\n積:{1}\n差:{2}".format(union, product, diff))
print('"se" in X? ', "se" in Xset)
print('"se" in Y? ', "se" in Yset)
