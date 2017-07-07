import pickle
model92 = pickle.load(open("cosine92.pickle","rb"))
correct = []
wrong = []
for line in model92:
    line = line.strip("\n").split(" ")
    y = line[3]
    y_ = line[4]
    if  y == y_:
        correct.append(y)
    else:
        wrong.append("{}\t{}".format(y,y_))
correct_prob = len(correct)/len(model92)
print(correct_prob)
