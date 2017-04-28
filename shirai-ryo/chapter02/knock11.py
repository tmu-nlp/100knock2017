f = open('hightemp.txt')
lines = f.read()

text = lines.replace('\t',' ')

print(text)
