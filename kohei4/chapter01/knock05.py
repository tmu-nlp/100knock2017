def my_ngram(l, n):
  ans = [ l[i:i+n ] for i in range( len(l) - n + 1) ]
  return ans

example = "I am an NLPer"
words = example.split()

print(my_ngram( words, 2 ))

for i in range(len(words)):
  print(my_ngram(words[i],2))
