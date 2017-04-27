def cipher(str):
	str2=''
	for i in range(len(str)):
		if 'a'<= str[i] <= 'z':
			str2 += chr(219-ord(str[i]))
		else:
			str2 += str[i]
	return str2

str1 = "aAbBc23"
print(cipher(str1))
	

				 
