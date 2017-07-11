import pickle

with open('data/answer85', 'rb') as i_f:
    words,vector = pickle.load(i_f)
print(vector[words['United_States']])
