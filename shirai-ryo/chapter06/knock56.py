#どういうことかわからないのであとで誰かに聞く


#できぬ

# import xml.etree.ElementTree as ET
# with open("nlp.txt.xml") as input_text: #, open("nlp_replace.txt.xlm", "w") as output_text:
#     tree = ET.parse(input_text)
#     root = tree.getroot()
#
#     root.findall(".//mention") = "representative mention(mention)"
#     tree.write("nlp_replace.xlm")


    # output_text.write(root.findall(".//mention"))


#コレジャナイ感が鬼

with open("nlp.txt.xml") as input_text:
    for line in input_text:
        if "<mention>" in line:
            line = line.replace("<mention>", "<representative mention(mention)>")
        print(line.strip("\n"))
