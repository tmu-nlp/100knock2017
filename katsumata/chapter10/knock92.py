import knock90
from gensim.models import word2vec
import pickle
import chapter09.knock88


if __name__ == '__main__':
    analogy_file = 'analogy.family'
    model = knock90.load_emb()
    with open('../chapter09/word_context_pca.dump', 'rb') as john:
        word_name, pca_matrix = pickle.load(john)

    with open(analogy_file) as i_f, open('analogy.ans90','w') as o_f:
        for line in i_f:
            one,two,drei,ans=line.strip().split()
            if not (one in model and two in model and drei in model):
                continue
            x = model.most_similar(positive=[two,drei], negative=[one])
            o_f.write('{}\t{} {}\n'.format(line.strip(), x[0][0], x[0][1]))
    with open(analogy_file) as i_f, open('analogy.ans85', 'w') as o_f:
        for line in i_f:
            one,two,drei,ans=line.strip().split()
            if not (one in word_name and two in word_name and drei in word_name):
                continue
            vec_one=pca_matrix[word_name[one]]
            vec_two=pca_matrix[word_name[two]]
            vec_drei=pca_matrix[word_name[drei]]
            vec_arg=vec_two+vec_drei-vec_one
            top_list = knock88.make_rank(vec_arg, word_name, pca_matrix)
            o_f.write('{}\t{} {}\n'.format(line.strip(),top_list[0][0], top_list[0][1])) 
