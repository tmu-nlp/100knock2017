from gensim.models import *
import pickle
features = pickle.load(open("features85.pickle","rb"))
model = word2vec.Word2Vec.load('corpus90.model')
'''
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し
index 1 - 0 + 2
'''
def read(f):
    for l in open(f):
        yield l
        
answer = []
for line in read("model91.txt"):
    if ":" in line: # skip topic
        continue
    line = line.strip("\n")
    words = line.split(" ")
    if words[0] not in features or words[1] not in features or  words[2] not in features:
        continue
    name,cosine = model.wv.most_similar(positive=[words[1], words[2]], negative=[words[0]])[0] # [0] is the highest score
    new_line = "{} {} {}".format(line,name,cosine)
    print(new_line)
    answer.append(new_line)
pickle.dump(answer,open("cosine92.pickle","wb"))
