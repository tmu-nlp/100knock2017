def my_ngram(l, n):
  ans = [ l[i:i+n ] for i in range( len(l) - n + 1) ]
  return ans

example1 = "paraparaparadise"
example2 = "paragraph"

X = set(my_ngram(example1,2))
Y = set(my_ngram(example2,2))

print("X =", X)
print("Y =", Y)
print("X | Y =", X | Y )
print("X & Y =", X & Y )
print("X - Y =", X - Y )
print("'se' in X ?", 'se' in X)
print("'se' in Y ?", 'se' in Y)
