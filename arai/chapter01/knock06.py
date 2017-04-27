def n_gram(text,n):
        result = []
        for i in range(len(text)-n+1):
                result.append(text[i:i+n])
        return result

x = n_gram('paraparapradise', 2)
y = n_gram('paragraph', 2)

X = set(x)
Y = set(y)

print(X|Y)
#和集合
print(X-Y)
#差集合
print(X&Y)
# 積集合

if "se" in  x:
	print("xにある")
if "se" in y:
	print("yにある")

