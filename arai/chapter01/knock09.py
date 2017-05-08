import random

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
sentence=sentence.replace(",","").replace(".","")
words=sentence.split(" ")
new_words=''
for i in words:
	if 4<len(i):
		new_words+=i[0]
		x=random.sample(range(1,len(i)-1),len(i)-2)
		for e in x:
			new_words+=i[e]
		new_words+=i[len(i)-1]
	else:
		new_words+=i
	print(new_words, end=' ')
	new_words=''
