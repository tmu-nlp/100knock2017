def cipher(text):
	result = ""
	for i in range(len(text)):
		if ord('a') <= ord(text[i]) <= ord('z'):
			a = ord(text[i])
			b = chr(219 - a)
			result += b
		else:
			result += text[i]
	return result


tmu = "Tokyo Metropolitan University"
tmu_2 = cipher(tmu)
#暗号化
print(tmu_2)
#復号化
print(cipher(tmu_2))	
