if __name__ == '__main__':
    answer = []
    with open('data/answer91.txt') as i_f1:
        for line in i_f1:
            elements = line.strip().split()
            answer.append(elements[3])
#    print(answer)
    with open('data/answer92_85.txt') as i_f2:
        counter = 0
        for i,line in enumerate(i_f2):
            line = line.lower()
            elements = line.strip().split()
            if elements[1] == answer[i]:
                counter += 1
        print('85\t{}'.format(counter/len(answer)))
    with open('data/answer92_90.txt') as i_f3:
        counter = 0
        for i,line in enumerate(i_f3):
            line = line.lower()
            elements = line.strip().split()
            if elements[1] == answer[i]:
                counter += 1
        print('90\t{}'.format(counter/len(answer)))
