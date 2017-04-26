import sys

with open('hightemp.txt') as f:
    w = f.readlines()
print("inputList: ", w)
lineno = len(w)
print("lof: ", lineno)

arg = sys.argv
try:
    N = int(arg[1])
except ValueError:
    print("Could not convert to integer.")
    exit(1)

residual = lineno % N
line_per_file = lineno // N
if residual == 0:#等分できるとき
    print("line_per_file: ", line_per_file)
    # Note 等分割できるので、単純にファイル全体の行を要素とするリストをN等分
    a = [w[x:x+line_per_file] for x in range(0, lineno, line_per_file)]
    print(" ============  solution. ===============")
    print("input N = ", N)
    for l in a:
        print(l)
else:#等分できないとき
    # 元リストを先頭からline_per_fileずつとってきて、N個のリストをつくる
    a1 = w[0:lineno - residual]
    a2 = w[lineno - residual:]
    # まずa1をN分割
    g = [a1[x:x + line_per_file] for x in range(0, len(a1), line_per_file)]
    # 元リストののこり要素を、N個のリストのどれかに適当にappendする.ここでは先頭から一つずつappendする。（残り要素数<Nは必ず真）
    for (i,v) in enumerate(a2):
        g[i].append(v)
    print(" ============  solution. ===============")
    print("input N = ", N)
    print("length of result list = ", len(g))
    for l in g:
        print(l)