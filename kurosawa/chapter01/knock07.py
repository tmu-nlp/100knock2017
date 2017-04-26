def make_str(x,y,z):
    str1 = ""
    str1 += str(x)
    str1 += "時の"
    str1 += str(y)
    str1 += "は"
    str1 += str(z)
    return str1

x = 12
y = "気温"
z = 22.4
print(make_str(x,y,z))
