sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

direct = [1, 5, 6, 7, 8, 9, 15, 16, 19]

element = dict()
for i, word in enumerate(sentence.strip().split()):
    if i + 1 in direct:
        element[word[0]] = i + 1
    elif i + 1 == 12:
        element[word[0:3:2]] = i + 1
    else:
        element[word[:2]] = i + 1

print(sorted(element.items(), key=lambda x:x[1]))
