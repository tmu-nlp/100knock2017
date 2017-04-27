def string1(x,y,z):
#    str1 = ("%d時の%sは%.1f" % (x,y,z))
    str1 = ("{0}時の{1}は{2}".format(x,y,z))
    return str1
print(string1(12,"気温",22.4))
