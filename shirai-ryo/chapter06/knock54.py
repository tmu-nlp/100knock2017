import xml.etree.ElementTree as ET
with open("nlp.txt.xml") as input_text:
    tree = ET.parse(input_text)
    root = tree.getroot()

    w = root.findall(".//word")
    l = root.findall(".//lemma")
    p = root.findall(".//POS")

    for word, lemma, pos in zip(w, l, p):
        print("{}\t{}\t{}".format(word.text, lemma.text, pos.text))
