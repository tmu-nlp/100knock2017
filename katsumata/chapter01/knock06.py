#単語n-gram
"""
def word_n_gram(n, str1):
    list_w_ngram = []
    str2 = str1.split()
    for i in range(len(str2)-(n-1)):
        list_w_ngram.append(str2[i:i+n])
    return list_w_ngram
"""
#文字n-gram
def char_n_gram(n, str1):
    list_char_ngram = []
    for i in range(len(str1)-(n-1)):
        list_char_ngram.append(str1[i:i+n])
    return list_char_ngram

str1 = 'paraparaparadise'
str2 = 'paragraph'
print ('paraparaparadise')
print (char_n_gram(2, str1))
print ('paragraph')
print (char_n_gram(2, str2))

X = set(char_n_gram(2, str1))
Y = set(char_n_gram(2, str2))

print ('和集合')
print (X | Y)
print ('積集合')
print (X & Y)
print ('差集合X-Y')
print (X - Y)
print ('差集合Y-X')
print (Y - X)


if 'se' in X and 'se' in Y:
    print ('include "se"')
else:
    print ('not include "se"')


"""
if 'se' in X:
    print ('include "se" in X')
    flag_X = 1
else:
    flag_X = 0
if 'se' in Y:
    print ('include "se" in Y')
    flag_Y = 1
else:
    flag_Y = 0
if flag_X == 0 and flag_Y == 0:
    print ('not include')
"""
