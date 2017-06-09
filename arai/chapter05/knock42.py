from knock41 import Chunk
from knock41 import cabocha_data

for line in cabocha_data():
    for word in line:
        #print(word.printsurface(), word.dst, word.srcs)
        if word.dst  != -1:
            print(''.join(word.get_word_only()) + '\t' + ''.join(line[word.dst].get_word_only()))
    
  
