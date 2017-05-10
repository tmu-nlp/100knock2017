origin_input="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
target = origin_input.replace(',', '').replace('.', '')
print([len(w) for w in target.split()])
