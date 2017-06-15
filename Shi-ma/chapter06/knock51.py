def split_sentence(data_in):
    for sentence in data_in:
        for word in sentence.split():
            yield word
        yield ''

if __name__ == '__main__':
    with open('knock50_result.txt', 'r') as data_in:
        with open('knock51_result.txt', 'w') as data_out:
            for word in split_sentence(data_in):
                print(word, file=data_out)
