def n_gram(n,content):
    return [content[i:i+n] for i in range(len(content)-n+1)]

sentence = "I am an NLPer"
words = sentence.split(" ")
bi = 2
print(n_gram(bi,sentence))
print(n_gram(bi,words))
