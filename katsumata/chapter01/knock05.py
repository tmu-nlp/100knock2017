#単語n-gram
def word_n_gram(n, str1):
    list_w_ngram = []
    str2 = str1.split()
    for i in range(len(str2)-(n-1)):
        list_w_ngram.append(str2[i:i+n])
    return list_w_ngram

#文字n-gram
def char_n_gram(n, str1):
    list_char_ngram = []
    #str1 = str1.replace(' ', '')
    for i in range(len(str1)-(n-1)):
        list_char_ngram.append([str1[i:i+n]])
    return list_char_ngram

string = 'I am an NLPer'
print ('単語bi-gram')
print (word_n_gram(2, string))
print ('文字bi-gram')
print (char_n_gram(2, string))
