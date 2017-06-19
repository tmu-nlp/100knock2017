from knock50 import split_sentence
def split_word():
    for line in split_sentence():
        words = line.split()
        for word in words:
            yield (word)
        yield '' 
if __name__ == '__main__':
    for word in split_word():
        print(word)

