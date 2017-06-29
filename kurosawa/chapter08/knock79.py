import pickle
import pylab as pl
from sklearn.metrics import precision_recall_curve

if __name__ == '__main__':
    ids_file = 'feature.ids'
    ans_file = '76ans.txt'

    with open(ids_file,'rb') as ids_data, open(ans_file) as ans:
        ids = pickle.load(ids_data)
        y = []
        y_ = []
        for line in ans:
            line = line.split('\t')
            y.append(int(line[0]))
            y_.append(float(line[2]))
    p,r,th = precision_recall_curve(y,y_)
    
    pl.clf()
    pl.plot(r,p, label='Precision-Recall curve')
    pl.xlabel('recall')
    pl.ylabel('Precision')
    pl.ylim([0.0, 1.05])
    pl.xlim([0.0, 1.0])
    pl.title('Precision-Recall')
    pl.legend(loc='lower left')
    pl.show()
