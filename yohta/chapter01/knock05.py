def Ngram(str,n):

#  str = "I am an NLPer"
#  n = 2

    ngram = []
    for i in range(len(str)):
        cw = ""
        if i >= n - 1:
#            for j in range(n):
            for j in reversed(range(n)):
                cw += str[i - j]
        else:
                continue
        ngram.append(cw)
    return ngram

s = "I am an NLPer"
str1 = s.replace(" ","")
str1 = Ngram(str1,2)
print ("文字bi-gram:",str1)
str2 = s.split()
str2 = Ngram(str2,2)
print ("単語bi-gram:",str2)


#    if i >= n-1:
#      for j in reversed(range(n)):
#        cw += str[i-j]
##      continue
