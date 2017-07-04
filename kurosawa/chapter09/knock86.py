import pickle

if __name__ == '__main__':
    with open('85_feature','rb') as data:
        feature = pickle.load(data)
    print(feature['United_States'])
