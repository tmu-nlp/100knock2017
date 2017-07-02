import random
import pickle
def read(f):
    for l in f:
        yield l
if __name__ == "__main__":
    corpus = pickle.load(open("corpus81.pickle","rb"))
result = []
'''
I have a pen,  d = 2 , target = have
have I -> front
have a -> back
have pen -> front
'''
for line in read(corpus):
    words = line.strip("\n").split()
    for i in range(len(words)):
        d = random.randint(1, 5)
        for j in range(i-d, i+d+1,1):
            if j >= 0 and j < len(words) -1 and j != i: # not out of index and j is "i" itself
                r =  "{}\t{}".format(words[i],words[j])
                result.append(r)
pickle.dump(result,open("tokens82.pickle","wb"))
print("finished")
