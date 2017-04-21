import re
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

str1 = filter(lambda w: len(w) >0,re.split('\s|,|\.|',str))
counter = 1
initial = {}
#print str1[0]
for c in str1:
    initial = {counter:c}
    if counter == 1 or 4 < counter < 10 or 14 < counter < 17 or counter == 19:
        m = c[:1]
    else:
        m = c[:2]
    initial = {counter:m}
    print initial
    counter += 1
