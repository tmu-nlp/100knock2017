import pickle
from scipy import spatial
from collections import defaultdict

if __name__ == '__main__':
    with open('85_feature','rb') as data:
        x = pickle.load(data)
    dis = defaultdict(float)
    for co in x.keys():
        if co != 'England':
            dis[co] = spatial.distance.cosine(x['England'],x[co])
    i = 0
    for co, val in sorted(dis.items(),key=lambda x: x[1]):
        print('{}:{}'.format(co,1-val))
        i += 1
        if i >=10:
            break

