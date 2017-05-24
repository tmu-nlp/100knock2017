with open('UKdata.txt', 'r') as input_data:
    for line in input_data:
        for i in range(len(line) - 7):
            if(line[i:i+8] == 'Category'):
                print(line)
