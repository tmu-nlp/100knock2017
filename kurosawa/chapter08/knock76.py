import pickle
from knock72 import make_sentence_feature

if __name__ =='__main__':
    lo_file = 'model.log'
    ids_file = 'feature.ids'
    test_file = 'sentiment.txt'
    ans_file = '76ans.txt'
    with open(lo_file, 'rb') as model, open(ids_file, 'rb') as ids_data:
        lo = pickle.load(model)
        ids = pickle.load(ids_data)
    with open(test_file) as test, open(ans_file,'w') as ans:
        for line in test:
            y, sen = line.split('\t')
            x = [make_sentence_feature(sen, ids)]
            ans.write('{}\t{}\t{}\t{}'.format(y,lo.predict(x)[0],lo.predict_proba(x)[0][1],sen))

