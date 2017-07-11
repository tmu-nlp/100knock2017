

if __name__ == '__main__':
    with open('family_92_85.txt') as data:
        same = 0
        num = 0
        for line in data:
            num += 1
            line = line.split()
            if line[3] == line[4]:
                same += 1
    print('85accuracy:{}'.format(same/num))
    with open('family_92.txt') as data:
        same = 0
        num = 0
        for line in data:
            num += 1
            line = line.split()
            if line[3] == line[4]:
                same += 1
    print('90accuracy:{}'.format(same/num))

