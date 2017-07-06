import pickle
import numpy as np
import knock87

def make_rank(word_vec, word_name, pca_matrix, ex_name=''):
    top_list = list()
    for word in word_name:
       if word == ex_name:
           continue
       top_list.sort(key=lambda x:x[1], reverse=True) 
       v = pca_matrix[word_name[word]]
       temp_sim = knock87.cos_sim(word_vec, v)
       if len(top_list) < 10:
           top_list.append((word, temp_sim))
       else:
            if top_list[9][1] < temp_sim:
                top_list[9] = (word, temp_sim)
    return top_list            
        

if __name__ == '__main__':
    with open('word_context_pca.dump', 'rb') as i_f:
        word_name, pca_matrix = pickle.load(i_f)
    vec_Eng = pca_matrix[word_name['England']]
    """
    for word in word_name:
        if word == 'England':
            continue
        top_list.sort(key=lambda x:x[1], reverse=True)
        vec_word = pca_matrix[word_name[word]]
        temp_sim = knock87.cos_sim(vec_Eng, vec_word)
        if len(top_list) < 10:
            top_list.append((word, temp_sim))
        else:
            if top_list[9][1] < temp_sim:
                top_list[9] = (word, temp_sim)
    """
    print('Englandに近い単語')
    for word, sim in make_rank(vec_Eng, word_name, pca_matrix, 'England'):
       print ('{}\t{}'.format(word, sim)) 

