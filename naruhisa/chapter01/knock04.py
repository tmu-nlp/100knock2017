str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

charcount = 0
tmpword = ''
wordcount = 1
dict = {}
for i in range(len(str)):
	if(str[i] == ' ' ):
		print(tmpword, wordcount)
		dict[wordcount] = tmpword
		charcount = 0
		wordcount += 1
		tmpword = ''
	elif((str[i] == ',' or str[i] == '.')):
		pass

	else:
		if (wordcount == 1 or 5 <= wordcount <= 9 or wordcount == 15 or wordcount == 16 or wordcount == 19):
			if(charcount == 1):
				continue
				
		else:
			if(charcount == 2):
				continue

		tmpword +=  str[i]
		charcount += 1

print(tmpword, wordcount)
dict[wordcount] = tmpword
