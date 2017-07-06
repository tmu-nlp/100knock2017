import pickle

if __name__ == '__main__':
    corpus_file = 'corpus_80.txt'
    country_file = 'country.pickle'
    with open(country_file,'rb') as f:
        country_list = pickle.load(f)
    with open(corpus_file) as f,open('corpus_81.txt','w') as co:
        for i, line in enumerate(f):
            if i%10000 == 0:
                print(i)
            for j in country_list:
                line = line.replace(j, '_'.join(j.split()))
            co.write('{}'.format(line))
#            if i ==10:
#                break
