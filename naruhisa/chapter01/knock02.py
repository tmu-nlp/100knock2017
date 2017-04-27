str1 = 'パトカー'
str2 = 'タクシー'

for i in range(min(len(str1), len(str2))):
	print(str1[i]+ str2[i], end="")
print()
