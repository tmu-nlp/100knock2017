import pickle
import knock87
import knock90
from gensim.models import word2vec

if __name__ == '__main__':
    model = knock90.load_emb()
    sim_file = 'wordsim353/combined.tab'
    with open('../chapter09/word_context_pca.dump', 'rb') as john:
        word_name, pca_matrix = pickle.load(john)
        
    with open(sim_file) as i_f, open('similarity.90', 'w') as o_f:
        for i,line in enumerate(i_f):
            if i == 0:
                continue
            one, zwei, mean = line.strip().split()
            if not (one in model and zwei in model):
                continue
            o_f.write('{}\t{}\n'.format(line.strip(),knock87.cos_sim(model[one],model[zwei])))

    with open(sim_file) as i_f, open('similarity.85', 'w') as o_f:
        for i,line in enumerate(i_f):
            if i== 0:
                continue
            one,zwei,mean=line.strip().split()
            if not (one in word_name and zwei in word_name):
                continue
            vec_one = pca_matrix[word_name[one]]
            vec_zwei=pca_matrix[word_name[zwei]]
            o_f.write('{}\t{}\n'.format(line.strip(), knock87.cos_sim(vec_one, vec_zwei)))
