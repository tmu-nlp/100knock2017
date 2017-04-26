def n_gram(text, n):
	result = []
	for i in range(len(text)-n+1):
		result.append(text[i:i+n])
	return result

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(n_gram(str1, 2))
Y = set(n_gram(str2, 2))

XY_wa = (X|Y)
XY_seki = (X&Y)
XY_sa = (X-Y)

print("X" + str(X))
print("Y" + str(Y))
print("和集合" + str(XY_wa))
print("積集合" + str(XY_seki))
print("差集合" + str(XY_sa))
if 'se' in X:
	print("'se'はXに含まれる")
if 'se' in Y:
	print("'se'はYに含まれる")

#TypeError: Can't convert 'set' object to str implicitly らしい

