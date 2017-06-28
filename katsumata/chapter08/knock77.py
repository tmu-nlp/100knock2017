def pre_rec_Fcalc(file_name):
    """
    index
    0:TP,1:FP,2:FN,3:TN
    """
    count = [0] * 4
    with open(file_name) as i_f:
        for line in i_f:
            #y_collect, y_prediction, probability
            y_co, y_pred, prob = line.strip().split()
            y_co = int(y_co)
            y_pred = int(y_pred)
            if y_co == 1:
                if y_pred == 1:
                    count[0] += 1
                else:
                    count[2] += 1
            else:
                if y_pred == 1:
                    count[1] += 1
                else:
                    count[3] += 1
    accuracy = (count[0] + count[3]) / sum(count)                   
    precision = count[0]/(count[0]+count[1])
    recall = count[0]/ (count[0] + count[2])
    F1 = 2*precision*recall/(precision + recall)
    return accuracy, precision, recall, F1

if __name__ == '__main__':
    file_name = 'knock76.txt'    
    acur, prec, rec, f1 = pre_rec_Fcalc(file_name)
    print ('正解率 {}\n適合率 {}\n再現率 {}\nF1 {}'.format(acur, prec, rec, f1))
    
