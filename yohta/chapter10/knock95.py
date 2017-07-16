from scipy.stats import spearmanr

def cal_spear(text):
    list_1 = []
    list_2 = []
    with open(text) as i_f:
        for line in i_f:
            list_1.append(line.strip().split()[2])
            list_2.append(line.strip().split()[3])
    return spearmanr(list_1,list_2)

if __name__ == '__main__':
    print ('answer_85')
    roh, p = cal_spear('data/answer94_85.txt')
    print (roh)
    print ('answer_90')
    roh, p = cal_spear('data/answer94_90.txt')
    print (roh)
