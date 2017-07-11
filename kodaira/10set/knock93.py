fname = "./data/similarity_knock92.txt"

score = 0
for line_count, line in enumerate(open(fname)):
  line = line.split()
  if line[3] == line[4]:
    score += 1

print("Accuracy: {:.2f}".format(score / line_count))

