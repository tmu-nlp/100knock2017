str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = []
str = str.replace(',','')
str = str.replace('.','')
str = str.split()
l = len(str)
for i in range(0,l):
    list.append(len(str[i]))
print(list)
