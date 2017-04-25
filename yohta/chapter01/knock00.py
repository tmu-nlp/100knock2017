str = "stressed"
str2 = ""
l = len(str)
for num in range(l):
    str2 += str[l - num - 1]
print(str2)
