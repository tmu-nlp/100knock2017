import re

def file_extend(file_name):
#    clean_list = ['.',',','!','?',';',':','(',')','[',']','\'','\"']
    with open(file_name) as f,open('corpus_80.txt','w') as corpus:
        for i, line in enumerate(f):
            line_new = []
            words = line.split()
            for word in words:
                word = re.sub('^[\.\,!\?;:\(\)\[\]\'\"]|[\.\,!\?;:\(\)\[\]\'\"]$','',word)
#                for clean_word in clean_list:
#                    word = word.replace(clean_word,'')
                if len(word) != 0:
                    line_new.append(word)
            corpus.write('{}\n'.format(' '.join(line_new)))
#            if i == 50:
#                break

if __name__ == '__main__':
    text_file_name = 'enwiki-20150112-400-r100-10576.txt'
    file_extend(text_file_name)
