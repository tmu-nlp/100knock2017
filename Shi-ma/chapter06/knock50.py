import re

def split_sentences(data_in):
    for phrases in data_in:
        sentence = []
        flag = 0
        phrases = phrases.split()
        for phrase in phrases:
            if phrase[-1] in '.:;!?':
                sentence.append(phrase)
                flag = 1
            elif flag == 1 and re.match(r'[A-Z]', phrase[0]):
                yield ' '.join(sentence)
                sentence = [phrase]
                flag = 0
            else:
                sentence.append(phrase)
        yield ' '.join(sentence)

if __name__ == '__main__':
    with open('../data/nlp.txt', 'r') as data_in:
        with open('knock50_result.txt', 'w') as data_out:
            for sentence in split_sentences(data_in):
                if sentence != '':
                    print(sentence, file=data_out)
