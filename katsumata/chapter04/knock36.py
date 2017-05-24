def make_frequency_dict():
    from knock30 import make_morpheme_list
    from collections import defaultdict
    morpheme_list = make_morpheme_list()
    frequency = defaultdict(int)

    for line in morpheme_list:
        for word in line:
            frequency[word['base']] += 1
    return (frequency)        

if __name__ == '__main__':
    frequency_dict = make_frequency_dict()
    for word, freq in sorted(frequency_dict.items(), key = lambda x:x[1], reverse = True):
        print ('{} : {}'.format(word, freq))
