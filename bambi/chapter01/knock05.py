def gram(n,content):
    return [content[i:i+n] for i in range(len(content)-n+1)]
    
sentence = "I am an NLPer"
words = sentence.split(" ")
bi = 2
print(gram(bi,sentence))
print(gram(bi,words))
