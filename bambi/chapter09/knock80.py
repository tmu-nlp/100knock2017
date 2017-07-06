import re
import pickle
def read_file(f):
    for line in open(f):
        yield line
if __name__ == "__main__":
    corpus = []
    # .,!?;:()[]'"　空文字列（empty_str,\n?\t?\r?)となったトークンは削除
    for line in read_file("enwiki-20150112-400-r100-10576.txt"):
        words = re.sub(r'[\.,!\?;:()\[\]\'"]*',r'',line).split()
        clean_out_empty_words = [w for w in words if len(w) > 0]
        corpus.append(" ".join(clean_out_empty_words))
        
    print(corpus[0:10])
    with open("corpus.txt", "w") as output:
        print(corpus,file=output)
    pickle.dump(corpus,open("corpus.pickle", "wb" ) )
    print("finished")
print(len(corpus))
