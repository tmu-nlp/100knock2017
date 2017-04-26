a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
b = a.split()

count = 1
for i in b:
	if count == 1 or 4 < count < 10 or 14<count<17 or count == 19:
		d = b[count-1][:1]
	else:
		d = b[count-1][:2]
	data = {count:d}
	print(data)
	count += 1
