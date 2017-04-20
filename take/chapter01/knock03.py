from collections import Counter

origin_input="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
target = origin_input.replace(',', '').replace('.', '')
result_list = []

for w in target.split():
    # print(w)
    result_list.append(len(w))
    # c = Counter(w)
    # # print(type(counter))
    # result = list(c)
    # # print(result)
    # print(c)
    # for word, count in c.most_common():
    #     print(word, count)

print(result_list)
