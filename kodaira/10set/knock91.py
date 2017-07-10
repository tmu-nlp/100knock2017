fname = "./data/questions-words.txt"
fout = "./data/family-words_knock91.txt"

w_pairs = open(fname).read().split(": ")
query = "family"
for block in w_pairs:
  if block.startswith(query):
    break

open(fout, 'w').write(block.replace("{}\n".format(query), ""))

