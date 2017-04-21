a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a = a.strip(',').strip('.')
b = a.split()
for i in range(len(b)):
   if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
       b[i] = b[i][0]
   else:
       b[i] = b[i][:2]

Element = {b[i]:i+1 for i in range(len(b))}

print(Element)

