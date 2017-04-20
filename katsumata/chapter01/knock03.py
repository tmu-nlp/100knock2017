str1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

count_num = []
str2 = str1.split()

for c in str2:
    count = 0
    for i in range(len(c)):
        count += 1
    if c[-1] == ',' or c[-1] == '.' :
        count -= 1
    count_num.append(count)
print (count_num)
