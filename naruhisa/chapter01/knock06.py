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

s1 = 'paraparaparadise'
s2 = 'paragraph'
s3 = 'se'
s1_bi = word_n_gram(2, s1)
s2_bi = word_n_gram(2, s2)

orset = s1_bi | s2_bi
andset = s1_bi & s2_bi
norset = s1_bi - s2_bi

print('s1set:', s1_bi)
print('s2set:', s2_bi)
print('和集合:', orset)
print('積集合:', andset)
print('差集合:', norset)
print('s1にseが含まれているか', s3 in s1_bi)
print('s2にseが含まれているか', s3 in s2_bi)
