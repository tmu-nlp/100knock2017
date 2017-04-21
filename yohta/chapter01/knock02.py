str1 = "パトカー"
str2 = "タクシー"
str = ""
print(str1)
print(str2)
for num in range(4):
    #a = 2 * num
    str += str1[num]
    str += str2[num]
print(str)
