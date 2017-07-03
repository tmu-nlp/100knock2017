import sys

def stopwords(str_):
    stopwords_list = ["a", "about", "am", "an", "and", "are", "as", "at", "be", "because", "by", "did", "do", "does", "had", "has", "have", "he", "i", "in", "is", "it", "of", "on", "she", "that", "the", "they"]
    
    if str_ in stopwords_list:
        return True
    else:
        return False

if __name__ == '__main__':
    str_ = sys.argv[1]
    print(stopwords(str_))
   
  
