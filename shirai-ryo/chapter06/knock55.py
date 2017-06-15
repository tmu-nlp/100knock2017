# <NER>PERSON</NER> の <word> が人名っぽい？

import xml.etree.ElementTree as ET
with open("nlp.txt.xml") as input_text:
    tree = ET.parse(input_text)
    root = tree.getroot()

    for ner, word in zip(root.findall(".//NER"), root.findall(".//word")):
        if ner.text == "PERSON":
            print(word.text)

    # ダメだったやつ
    # for ner in root.findall(".//NER"):
    #     for word in root.findall(".//word"):
    #         if ner.text == "PERSON":
    #             print(word.text)
    #
    # # ner.text == "PERSON"が1つでもあれば、wordが全部出て来ると言う処理になってしまう？
    # # たぶん
