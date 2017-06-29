import codecs
import random

pn_text = []

# codecsモジュールを使用すると、指定した文字コードでファイルを開くことができます。
pos_file = codecs.open("./rt-polarity.pos", "r", "utf-8", "ignore")
for line in pos_file:
    pos_line = "+1" + "\t" + line
    pn_text.append(pos_line)

neg_file = codecs.open("./rt-polarity.neg", "r", "utf-8", "ignore")
for line in neg_file:
    neg_line = "-1" + "\t" + line
    pn_text.append(neg_line)

random.shuffle(pn_text)

with open("sentiment.txt", "w") as output_text:
    for i in range(len(pn_text)):
        output_text.write(pn_text[i])

    # for line in pn_text:
    #   output_text.write(line)
    # こっちのほうが良いかも
