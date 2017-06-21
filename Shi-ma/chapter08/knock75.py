from sklearn.linear_model import LogisticRegression
import pickle


if __name__ == '__main__':
    with open('result/ids.dump', 'rb') as data_ids_in:
        ids = pickle.load(data_ids_in)
    with open('result/logistic.dump', 'rb') as data_logistic_in:
        logistic = pickle.load(data_logistic_in)

    weights = logistic.coef_[0]
    indexes_weights_sorted = sorted(enumerate(weights), key=lambda x: x[1], reverse=1)

    print('重みの高い素性トップ10')

    for index, weight in indexes_weights_sorted[:10]:
        print('{}\n{}'.format(sorted(ids.items(), key=lambda x: x[1])[index][0], weight))

    print('\n重みの低い素性トップ10')

    for index, weight in indexes_weights_sorted[-10:]:
        print('{}\n{}'.format(sorted(ids.items(), key=lambda x: x[1])[index][0], weight))
