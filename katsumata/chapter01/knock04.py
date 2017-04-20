str1 = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

dic = {}
str2 = str1.split()
print (str2)
#リストから1要素ずつ持ってきて、その要素と出現順を辞書に逐次追加していく
count = 1
for c in str2:
    if count == 1 or count == 5 or count == 6 or count == 7 or count == 8 or count == 9 or count == 15 or count == 16 or count == 19 :
        dic[c[0]] = count
    else:
        dic[c[0] + c[1]] = count
    count += 1
print (dic)
