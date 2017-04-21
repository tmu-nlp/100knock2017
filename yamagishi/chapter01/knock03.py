sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
sentence = sentence.replace(',', '').replace('.', '')

pi = [len(word) for word in sentence.strip().split()]
print(pi)
