from knock50 import get_sentence

for line in get_sentence():
    for word in line.split(' '):
        print(word.replace(',', '').replace('.', ''))
    print()
