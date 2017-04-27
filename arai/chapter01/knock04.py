sentence="He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sentence=sentence.replace(",","").replace(".","")
words=sentence.split(" ")
count= 1
for i in words:
	if count == 1 or 4<count<10 or 14<count<17 or count==19:
		a = words[count-1][:1]
	else:
		a = words[count-1][:2]
	b = {count:a}
	print(b)
	count+=1
	 
