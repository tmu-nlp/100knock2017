content = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = content.split()
result_dict = {}
for index, word in enumerate(words):
    key = ""
    if index % 2 == 0:
        key = word[:2]
    else:
        key = word[:1]
    result_dict[key] = index
print (result_dict)
