import random

def typo(w):
    if len(w) > 4:
        list1 = list(w[1:-1])
        random.shuffle(list1)
        result = w[0] + ''.join(list1) + w[-1]
    else:
        result = w
    return result


#    for i in range(len(s[i])):
#        if len(s[i]) <= 4:
#            str2[i] = ""
#        else:
#            str1[i] = ""
#            str2[i] = s[i]
#    for n in range(len(str1)):
#        if str1[n] == "":
#            str1[n] = str2[n]

#    for i in range(len(str1)):
#        if len(str1[i]) >= 4:
#            str2 = random.shuffle(str1)
#    return str2

#    list1 = list(filter(lambda x:len(x) <= 4,str1))
#    list2 = list(filter(lambda x:len(x) > 4,str1))
#    for i in list2[i]:
#        word = list(i[1:-2])
#        random.shuffle(word)
#        result1 = i[0] + ''.join(word) + i[-1]
#        result2 += result1

#    for n in range(len(list2)):
#        random.shuffle(list2[n])

#    list1 = list(list1)
#    list2 = list(list2)
#    random.shuffle(list1)
#    random.shuffle(list2)
#    str2 = list1 + list2
#    return result


str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."

result = ""
str1 = str1.replace("."," .")
s = str1.split()
for n in s:
    result += " " + typo(n)
print(result)
