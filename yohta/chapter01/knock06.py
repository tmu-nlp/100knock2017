def Ngram(str,n):

    ngram = []
    for i in range(len(str)):
        cw = ""
        if i >= n - 1:
            for j in reversed(range(n)):
                cw += str[i - j]
        else:
                continue
        ngram.append(cw)
    return ngram

str1 = "paraprapradise"
str2 = "paragraph"

bg1 = Ngram(str1,2)
bg2 = Ngram(str2,2)
set1 = set(bg1)
set2 = set(bg2)
union = set1 | set2
inter = set1 & set2
diff1 = set1 - set2
diff2 = set2 - set1

print("bigram-1(X):",bg1)
print("bigram-2(Y):",bg2)
print("X+Y:",union)
print("X*Y:",inter)
print("X-Y:",diff1)
print("Y-X:",diff2)
print("judge-X:",'se' in set1)
print("judge-Y:",'se' in set2)
