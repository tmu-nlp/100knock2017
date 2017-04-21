def ngram(str,n=2):
    l = len(str)
    for i in range(0,l-n+1):
        for j in range(0,n):
            print(str[i+j] + ' ',end='')
        print()
    print()

str = "I am an NLPer"
str1 = str.split()
ngram(str1)
str2 = str.replace(' ','')
strl = list(str2)
ngram(strl)
