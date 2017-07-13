if __name__ == '__main__':
    total_90 = 0
    total_85 = 0
    correct_90 = 0
    correct_85 = 0

    with open('ccc_cos90.txt', 'r') as i_f90, open('ccc_cos85.txt', 'r') as i_f85:
        for line in i_f90:
            words = line.strip().split()
            if words[3] == words[4]:
                correct_90 += 1
            total_90 += 1
        for line in i_f85:
            words = line.strip().split()
            if words[3] == words[4]:
                correct_85 += 1
            total_85 += 1

        print('model85:', float(correct_85 / total_85))
        print('model90:', float(correct_90 / total_90))
