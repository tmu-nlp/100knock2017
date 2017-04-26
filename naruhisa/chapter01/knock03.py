str = "Now I need a drink, alcholic of course, after the heavy lectures involving quantum mechanics."

charcount = 0
word = []

for i in range(len(str)):
	if(str[i] == ' '):
		print(charcount)
		word.append(charcount)
		charcount = 0

	elif(str[i] == ',' or  str[i] == '.'):
		pass

	else:
		charcount += 1
