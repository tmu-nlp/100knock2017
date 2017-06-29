from nltk.corpus import stopwords

def stop_word_check(word):
    stop_word_list = set(stopwords.words('english'))
    if word in stop_word_list:
        return True
    else:
        return False

def input_extend(line):
   words = line.split()
   for word in words:
       stop = stop_word_check(word)
       if stop is True:
           print('True({})'.format(word))
           break
   if stop is False:
       print('False')

if __name__ == '__main__':
    in_data = input('input word or sentence >> ')
    input_extend(in_data)
