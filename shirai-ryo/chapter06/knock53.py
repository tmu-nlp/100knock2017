import xml.etree.ElementTree as ET
with open("nlp.txt.xml") as input_text: #, open("fifteen_three_answer.txt", "w") as output_text:
    tree = ET.parse(input_text)
    root = tree.getroot()
    for word in root.findall(".//word"):
        # 子要素の取り出し find()は上から走査して最初に見つかったもの、findall()は全て
        print(word.text)
        #  output_text.write(word.text + "\n")
