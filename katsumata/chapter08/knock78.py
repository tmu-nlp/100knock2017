"""
'features.dump'にfeature_listがtag, 文, 素性が入ってる
knock73(train)のpredict_oneで推定、update_weightsで重みを更新
knock74にtest用のpredictがある
knock77にfile_name入力でaccuracyとprecision、recall,f1を出力するpre_rec_Fcalcがある
"""
import random
import pickle
from collections import defaultdict
import knock73
import knock76
import knock77

def c_Valid(d_list, d_num, th = .5):
    ac_list = [0]*d_num
    pre_list = [0]*d_num
    rec_list = [0]*d_num
    f1_list = [0]*d_num
    for i in range(d_num):
        test_list = list()
        train_list = list()
        for j in range(len(d_list)):
            if i == j:
                test_list = d_list[j]
            else:
                train_list += d_list[j]
        #train
        w = defaultdict(int)
        l = 10 
        for epoch in range(l):
            print ('d_num {} epoch {}'.format(i, epoch))
            random.shuffle(train_list)
            for y, x, phi in train_list:
                y_, prob = knock73.predict_one(w,phi, th)
                if y_ != int(y):
                    knock73.update_weights(w, phi, int(y))
        #test
        w = dict(w)
        ans_file = 'ans_file_' + str(i)
        with open(ans_file, 'w') as o_f:
            for t, y_pre, prob in knock76.predictFile(test_list, th, w):
                o_f.write('{}\t{}\t{}\n'.format(t, y_pre, prob))
        ac_list[i], pre_list[i], rec_list[i], f1_list[i] = knock77.pre_rec_Fcalc(ans_file)
        print ('正解率 {}\n適合率 {}\n再現率 {}\nF1 {}'.format(ac_list[i], pre_list[i], rec_list[i], f1_list[i]))
    return ac_list, pre_list, rec_list, f1_list
    
            

if  __name__ == '__main__':
    with open('features.dump', 'rb') as f_f:
        feature_list = pickle.load(f_f)
    div_num = 5
    l = len(feature_list) / div_num
    div_list = list()
    th = .5
    for i in zip(*[iter(feature_list)]*int(l)):
        div_list.append(i)
    ac, pre, rec, f1 = c_Valid(div_list, div_num, th)
    print ()
    print ('平均とった奴')
    print ('正解率 {}'.format(sum(ac)/div_num))
    print ('適合率 {}'.format(sum(pre)/div_num))
    print ('再現率 {}'.format(sum(rec)/div_num))
    print ('F1 {}'.format(sum(f1)/div_num))
