#!usr/bin/python

from collections import Counter
import pickle


fin = "./data/pair_knock82.txt"
pairs = open(fin, 'r')


co_occur_count = Counter()
context_count = Counter()
word_count = Counter()
count = 0


print("Count")
join_word = lambda context_word: "{}\t{}".format(word, context_word)
for line in pairs:
  line = line.strip().split('\t')
  word = line[0]; context_words = line[1:]
  word_count[word] += 1
  context_count.update(context_words)
  co_occur_count.update(map(join_word, context_words))


print("Save")
pickle.dump(dict(context_count), open('./data/context.pkl', 'wb'))
pickle.dump(dict(word_count), open('./data/word.pkl', 'wb'))
pickle.dump(dict(co_occur_count), open('./data/co_occur.pkl', 'wb'))
