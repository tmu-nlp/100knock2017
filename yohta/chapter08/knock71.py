from nltk.corpus import stopwords

sw = stopwords.words('english')

def return_TF(word):
    if word in sw:
        return True
    else:
        return False

if __name__ == '__main__':
    print('stopwords:')
    for i in range(len(sw)):
        print('{}'.format(sw[i]))

    word = input('insert sumple word:')
    print('{}'.format(return_TF(word)))
