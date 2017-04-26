s = 'I am an NLPer'

def word_n_gram(n, str):
	wordg = set()
	tmpword = ''
	for i in range(len(str)):
		if(str[i] == ' '):
			if (len(tmpword) >= n):
				for j in range(len(tmpword) - n + 1):
					if len(tmpword) < (j + n):
						break
					wordg.add(tmpword[j:j+n])

			else:
				pass

			tmpword = ''

		elif(str[i] == ',' or str[i] == '.'):
			pass

		else:
			tmpword += str[i]

	if (len(tmpword) >= n):
		for j in range(len(tmpword) + n + 1):
			if len(tmpword) < (j + n):
				break
			wordg.add(tmpword[j:j+n])
		tmpword = ''
	return wordg

def str_n_gram(m, str):
	strg = set()
	word = []
	tmpword = ''

	for i in range(len(str)):
		if(str[i] == ' ' or str[i] == ',' or str[i] == '.'):
			if(len(tmpword) == 0):
				continue
			word.append(tmpword)
			tmpword = ''
		else:
			tmpword += str[i]

	word.append(tmpword)
	tmpword = ''
	for j in range(len(word) - m + 1):
		for k in range(m):
			if tmpword == '':
				tmpword += word[k + j]
			else:
				tmpword += ' ' +  word[k + j]
		strg.add(tmpword)
		tmpword = ''
	return strg

print(word_n_gram(2, s))
print(str_n_gram(2, s))
