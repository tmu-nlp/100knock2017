import re
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

str1 = filter(lambda w: len(w) >0,re.split('\s|,|\.|',str))
#str2 = str1.split(",")
#str3 = str2.split(".")
print(str1)
for num in str1:
#    str2 = []
    str2 = len(num)
    print(str2),
#    ",".join(map(str2,list))
