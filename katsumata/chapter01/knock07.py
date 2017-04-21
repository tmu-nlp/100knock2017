def make_sent(x, y, z):
    str(x),str(y),str(z)
    return ('%s時の%sは%s'%(x,y,z))

x = 12 
y = '気温'
z = 22.4
print (make_sent(x, y, z))
