with open('UKdata.txt', 'r') as input_data:
    for line in input_data:
        for i in range(len(line) - 4):
            if(line[i:i+5] == 'File:' or line[i:i+5] == 'ファイル:'):
                text = ''
                for j in range(len(line)):
                    if j > i + 4:
                        if(line[j] == '|'):
                            break
                        text += line[j]
                print(text)
