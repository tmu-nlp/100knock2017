str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
dict = {}
num = [1,5,6,7,8,9,15,16,19]
str = str.replace('.','')
str = str.split()
l = len(str)
for i in range(0,l):
    if i+1 in num:
        dict[str[i][:1]] = i+1
    else:
        dict[str[i][:2]] = i+1
print(dict)
