import re
import pickle
def read(f):
    for l in open(f):
        yield l
if __name__ == "__main__":
    countries = []
    corpus = pickle.load(open("corpus.pickle","rb"))
    for c in read("country.txt"):
        c = c.strip("\n")
        # only 2 words++ will be recorded
        if len(c.split()) > 1:
            countries.append(c)
tokens = []
refined_corpus = []
for line in corpus:
    for c in countries:
        if c in line:
            r = re.sub(c,c.replace(" ","_"), line)
            line = r
    tokens += line.split()
    refined_corpus.append(line)
pickle.dump(tokens,open("token.pickle","wb"))
pickle.dump(refined_corpus,open("corpus81.pickle","wb"))
print("finished")
