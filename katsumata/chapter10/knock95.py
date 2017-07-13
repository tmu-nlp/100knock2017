from scipy.stats import spearmanr

def calcroh(file_name):
    human_list = list()
    pred_list = list()
    with open(file_name) as i_f:
        for line in i_f:
            human_list.append(line.strip().split()[2])
            pred_list.append(line.strip().split()[3])
    return spearmanr(human_list, pred_list)

if __name__ == '__main__':
    print ('spearmanr 90') 
    roh, p = calcroh('similarity.90')
    print (roh)
    print ('spearmanr 85')
    roh, p = calcroh('similarity.85')
    print (roh)
