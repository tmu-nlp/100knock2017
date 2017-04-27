def n_gram(text,n):
	result = []
	for i in range(len(text)-n+1):
		result.append(text[i:i+n])
	return result

sentence = "I am an NLPer"
word = sentence.split()
#文字
print(n_gram(sentence, 2))
#単語
print(n_gram(word, 2))

