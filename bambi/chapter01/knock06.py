def gram(n,content):
    return [content[i:i+n] for i in range(len(content)-n+1)]
raw_x = "paraparaparadise"
raw_y = "paragraph"
X = gram(2,raw_x)
Y = gram(2,raw_y)
print("X:{}".format(X))
print("Y:{}".format(Y))
union = list(set(X).union(Y))
intersection = list(set(X).intersection(Y))
difference_from_x = list(set(X).difference(Y))
difference_from_y = list(set(Y).difference(X))
print("和集合:{}".format(union))
print("積集合:{}".format(intersection))
print("差集合 in X not Y:{}".format(difference_from_x))
print("差集合 in Y not X:{}".format(difference_from_y))
def contain(target, data, set_name):
    status = "含まれない"
    if target in data: status = "含まれる"
    print(("{}は{}に{}").format(target,set_name,status))
target = "se"
contain(target,X,"X")
contain(target,Y,"Y")
