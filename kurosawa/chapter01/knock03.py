strin = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list1 = []
strin = strin.replace(',','')
strin = strin.replace('.','')
strin = strin.split()
l = len(strin)
for i in range(0,l):
    list1.append(len(strin[i]))
print(list1)
