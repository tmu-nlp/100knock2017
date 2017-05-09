content = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result = ""
words = content.replace(",", "").replace(".","").split()
for word in words:
    result += str(len(word))
print(result)
