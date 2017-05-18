with open('UKdata.txt', 'r') as input_data:

    for line in input_data:
        switch = 0
        for i in range(len(line)):
            if(line[i:i+2] == '=='):
                count = 1
                switch = 1
            elif(switch == 1 and line[i] == '='):
                count += 1
            elif(switch == 1 and line[i] != '='):
                print(i-1,line)
                break
