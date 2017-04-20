str = "パタトクカシーー"
str1 = ""
str2 = ""
l = len(str)
for num in range(l):
  if num % 2 == 0:
      str1 += str[num]
      continue
  str2 += str[num]
print(str1)
print(str2)
