from bs4 import BeautifulSoup, element
import nltk
soup = BeautifulSoup(open("nlp.txt.xml"),"lxml")
parsers = dependencies = soup.find_all('parse')
for p in parsers:
    tree = nltk.Tree.fromstring(p.text)
    for t in tree.subtrees(filter = lambda x: x.label() == "NP"):
        print(t)
