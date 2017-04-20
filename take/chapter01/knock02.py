a = 'パトカー'
b = 'タクシー'
alist = list(a)
blist = list(b)
result = ''
for x, y in zip(alist, blist):
    result += x + y
    if len(result) == len(alist) + len(blist):
        print(result)