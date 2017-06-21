from nltk.corpus import stopwords

if __name__ == '__main__':
    stopwords_set = set(stopwords.words('english'))
    test_txt = 'an idealistic love story that brings out the latent 15-year-old romantic in everyone . '
    test_txt = test_txt.lower()
    result_txt = []

    for word in test_txt.split():
        result = lambda word: '{}'.format(int(word in stopwords_set)).rjust(len(word))
        result_txt.append(result(word))

    print(test_txt)
    print(' '.join(result_txt))
