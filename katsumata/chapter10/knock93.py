

def getAcu(file_name):
    denominator=0 #分母
    numerator=0 #分子
    with open(file_name) as i_f:
        for line in i_f:
            elements=line.strip().split()
            denominator += 1
            if elements[3]==elements[4]:
                numerator += 1
    return numerator, denominator

if __name__ == '__main__':
    #85
    nume, denomi = getAcu('analogy.ans85')
    print ('accuracy_85')
    print ('分母{} 分子{}'.format(denomi, nume))
    print ('accuracy {}'.format(nume/denomi))

    #90
    john, wick = getAcu('analogy.ans90')
    print ('accuracy_90')
    print ('分母{} 分子{}'.format(wick,john))
    print ('accuracy {}'.format(john/wick))

