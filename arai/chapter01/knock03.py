sentence="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence=sentence.replace(",","").replace(".","")
words = sentence.split(" ")
for i in range (len(words)):
	print(len(words[i]),end="")

