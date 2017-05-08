with open('hightemp.txt','r') as f:
    n = int(input('N > '))
    i = 0
    for line in f:
        if i % n ==0:
            print()
        print(line, end="")
        i += 1

