import matplotlib.pyplot as plt
import pickle
import knock78

if __name__ == '__main__':
    th = 0
    with open('features.dump', 'rb') as f_f:
        feature_list = pickle.load(f_f)
    div_num = 5
    l = len(feature_list)/div_num
    div_list = list()
    for i in zip(*[iter(feature_list)]*int(l)):
        div_list.append(i)

    pre_list = list()
    rec_list = list()

    for i in range(11):
        print ('閾値')
        print (th)
        print ()
        ac, pre, rec, f1 = knock78.c_Valid(div_list, div_num, th)
        ave_pre = sum(pre) / div_num
        ave_rec = sum(rec) / div_num
        pre_list.append(ave_pre)
        rec_list.append(ave_rec)
        th += .1
    plt.plot(rec_list, pre_list, marker='o', markeredgewidth=0)
    print ('recoll')
    print (rec_list)
    print ('precision')
    print (pre_list)
    plt.title('pre-reco graph')
    plt.xlabel('Recoll')
    plt.ylabel('Precision')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.01])
    plt.grid(True)
    plt.show()
