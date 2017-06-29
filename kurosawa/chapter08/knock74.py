import pickle
from knock72 import make_sentence_feature


if __name__ =='__main__':
    lo_file = 'model.log'
    ids_file = 'feature.ids'
    with open(lo_file, 'rb') as model, open(ids_file, 'rb') as ids_data:
        lo = pickle.load(model)
        ids = pickle.load(ids_data)

    x = [make_sentence_feature(input('>>'),ids)]
    print(lo.predict_proba(x))
