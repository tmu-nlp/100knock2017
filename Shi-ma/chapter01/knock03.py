txt = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = txt.replace(',', ' ').replace('.', ' ').split()
ans = []

for word in words:
    ans.append(len(word))

print(ans)
