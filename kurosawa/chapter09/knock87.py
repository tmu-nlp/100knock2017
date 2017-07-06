import pickle
from scipy import spatial

if __name__ == '__main__':
    with open('85_feature','rb') as data:
        x = pickle.load(data)
    sim = 1 - spatial.distance.cosine(x['United_States'],x['U.S'])
    print(sim)

