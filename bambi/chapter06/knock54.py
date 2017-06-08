from bs4 import BeautifulSoup
soup = BeautifulSoup(open("nlp.txt.xml"),"lxml")# lxml mode is faster but need to install
tags = soup.find_all(["word","lemma","pos"])
result = []
content = ""
for tag in tags:
    if tag.name == "word":
        if len(content) > 0:
            result.append(content[1:]) # remove first charcter (/)
            content = ""
    content += "/" + tag.text
print(result)
