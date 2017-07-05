from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

answer = []
predict = []
for line in open('knock76_file.txt'):
    line = line.strip().split()
    answer.append(int(line[0]))
    predict.append(int(line[1]))
    
print('accuracy: {}'.format(accuracy_score(answer, predict)))
print('precision: {}'.format(precision_score(answer, predict)))
print('recall: {}'.format(recall_score(answer, predict)))
print('F1: {}'.format(f1_score(answer, predict)))
