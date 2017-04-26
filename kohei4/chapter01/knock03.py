a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
a = a.strip(',').strip('.')
b = a.split()
pai = []
for i in range(len(b)):
  pai.append(len(b[i]))
print(pai)
