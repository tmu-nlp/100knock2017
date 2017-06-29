from sklearn.metrics import precision_recall_fscore_support

def print_data(y,y_):
    p,r,f,s = precision_recall_fscore_support(y,y_)
    print('precision:\t{}'.format(p[1]))
    print('recall:\t\t{}'.format(r[1]))
    print('f1 score:\t{}'.format(f[1]))

if __name__ == '__main__':
    ans_file = '76ans.txt'
    with open(ans_file) as ans:
        y = []
        y_ = []
        for line in ans:
            line = line.split('\t')
            y.append(line[0])
            y_.append(line[1])
        print_data(y, y_)
