def ngram(str,n=2):
    l = len(str)
    list= []
    strsub = ""
    for i in range(0,l-n+1):
        for j in range(0,n):
            strsub += str[i+j]
        list.append(strsub)
        strsub = ""
    return list

str1 = "paraparaparadise"
str2 = "paragraph"
list1 = list(str1)
list2 = list(str2)
x = set(ngram(list1))
y = set(ngram(list2))
wa = x.union(y)
seki = x.intersection(y)
sa1 = x.difference(y)
sa2 = y.difference(x)
print(wa)
print(seki)
print(sa1)
print(sa2)
print('se' in seki)
