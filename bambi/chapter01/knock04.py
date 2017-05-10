content = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = content.split()
result_dict = {}
for index, word in enumerate(words):
    key = ""
    if index + 1 not in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        key = word[:2]
    else:
        key = word[:1]
    result_dict[key] = index + 1
print (sorted(result_dict.items(), key=lambda x:x[1]))
