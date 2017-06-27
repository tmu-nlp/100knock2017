import collections
import numpy as np

label = list()
pred = list()
prob = list()

with open('knock76.out') as f:
    for l in f:
        _label, _pred, _prob = l.split('\t')
        label.append(int(_label))
        pred.append(int(_pred))
        prob.append(float(_prob))

correct = np.array(label) * np.array(pred)
correct_count = collections.Counter(correct)

accuracy = correct_count[1]/(correct_count[-1]+correct_count[1])
print("accuracy: {} ".format(accuracy))

#recall
# 正解ラベルが1について
# 1と予測した
# -1と予測した

pred_pos = 0
pred_neg = 0
lab_pos = 0
lab_neg = 0

for (l, p) in zip(label, pred):
    if l == 1:
        if p == 1:
            pred_pos += 1
        else:
            pred_neg += 1

    if p == 1:
        if l == 1:
            lab_pos += 1
        else:
            lab_neg += 1

'''
TODO
recallとprecisionの定義が逆っぽい
あとでなおす
'''
recall = pred_pos/(pred_neg + pred_pos)
print("reacll for pos: {} ".format(recall))


#precision
# 1と予測したもののうち、正解が1と-1のもの

precision = lab_pos/(lab_pos + lab_neg)
print("precision for pos: {} ".format(precision))



from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
prec_skl = precision_score(label, pred)
recal_skl = recall_score(label, pred)
acc = accuracy_score(label, pred)
f1 = f1_score(label, pred)
print('\ncomputed by sklearn\n')
print('prec: {}\nrecall: {}\naccuracy: {}\nf1 :{}'.format(prec_skl, recal_skl, acc, f1))




