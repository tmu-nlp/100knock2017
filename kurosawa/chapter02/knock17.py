with open("hightemp.txt",'r') as f:
    col1 = []
    for list in f:
        list = list.split()
        if not(list[0] in col1):
            col1.append(list[0])
    print(col1)
