from nltk import stem
stemmer = stem.PorterStemmer()

with open("fifteen_one_answer.txt") as text:
    for words in text:
        words = words.strip("\n")
        #前処理でミスしやすい点なので注意
        words = words.strip(".")
        print(stemmer.stem(words))
