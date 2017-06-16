import re

def get_sentence():
    with open('nlp.txt', 'r') as f:
        for line in f:
            tmp = 0
            pettern = re.compile(r'[\:\.\;\!\?] [A-Z]')
            iterator = pettern.finditer(line)
            for sentence in iterator:
                yield line[tmp:sentence.end() - 1]
                tmp = sentence.end() - 1
            yield line[tmp:]

if __name__ == '__main__':
    for line in get_sentence():
        print(line)
