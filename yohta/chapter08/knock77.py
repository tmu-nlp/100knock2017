from knock72 import pn_list
from knock76 import pl_list
#from sklearn.metrics import confusion_matrix

def confmat_status(true_list,pre_list):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(len(true_list)):
        if true_list[i] == pre_list[i]:
            if true_list[i] == 1:
                tp += 1
            else:
                tn += 1
        else:
            if true_list[i] == 1:
                fn += 1
            else:
                fp += 1
#    return [tp,tn,fp,fn]

    acc = (tp + tn) / (tp + tn + fp + fn) # 正解率
    pre = tp / (tp + fp) # 適合率
    rec = tp / (tp + fn) # 再現率
    f1 = 2 * pre * rec / (pre + rec)
    return [acc,pre,rec,f1]

if __name__ == '__main__':
    result = confmat_status(pn_list,pl_list)
    print('正解率:{}\n適合率:{}\n再現率:{}\nf1_score:{}'.format(result[0],result[1],result[2],result[3]))


#    print(tp)
#    print(tn)
#    print(fp)
#    print(fn)
#    print(tp+tn+fn+fp)
