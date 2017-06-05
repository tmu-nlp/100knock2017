from bs4 import BeautifulSoup
soup = BeautifulSoup(open("nlp.txt.xml"),"lxml")# lxml mode is faster but need to install
print(soup.prettify())
