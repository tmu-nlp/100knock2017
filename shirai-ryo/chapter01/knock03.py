a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
a_2 = a.replace(",", "").replace(".", "")  
b = a_2.split()

for i in range(len(b)):
	print(len(b[i]),end="")
