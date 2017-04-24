from string import Template

def hoge_func(p):
    t = Template('$x時の$yは$z')
    return t.substitute(p)

if __name__ == '__main__':
    params = {'x':12, 'y':'気温', 'z':22.4}
    print(hoge_func(params))