from bs4 import BeautifulSoup, element
soup = BeautifulSoup(open("nlp.txt.xml"),"lxml")
tokens = soup.find_all('tokens')
'''
  <token id="4">
            <word>Alan</word>
            <lemma>Alan</lemma>
            <CharacterOffsetBegin>636</CharacterOffsetBegin>
            <CharacterOffsetEnd>640</CharacterOffsetEnd>
            <POS>NNP</POS>
            <NER>PERSON</NER>
            <Speaker>PER0</Speaker>
          </token>
'''
if tokens is not None:
    for token in tokens:
        children = token.children
        for child in children:
            ner = child.find("ner") # ner = Named Entity Recognition
            if isinstance(ner,element.Tag): # only tag object can pass, the other like "\n", bye bye 
                if ner.text.lower() == "person":
                    print(child.find("word").text)
