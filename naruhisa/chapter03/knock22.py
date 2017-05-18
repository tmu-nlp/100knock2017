with open('UKdata.txt', 'r') as input_data:
    for line in input_data:
        for i in range(len(line) - 7):
            if(line[i:i+8] == 'Category'):
                text = ''
                for j in range(len(line)):
                    if j > i + 8:
                        if(line[j] == ']'):
                            break
                        text += line[j]
                print(text)
