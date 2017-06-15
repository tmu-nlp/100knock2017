import xml.etree.ElementTree as ET

def make_corenlp_word(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    for sentence in root.findall(".//sentences/sentence"):
        for word in sentence.findall(".//tokens/*/word"):
            print(word.text, file=data_out)
        print('', file=data_out)

if __name__ == '__main__':
    with open('knock53_result.txt', 'w') as data_out:
        data_in_path = '../data/knock50_result.txt.xml'
        make_corenlp_word(data_in_path, data_out)

# 普通に nlp.txt を StanfrdCoreNLP で解析するとピリオド区切りになってしまうため、knock50 で作った一行一文形式のファイルを以下のオプションで実行し、一文区切りで解析した。
# java -cp stanford-corenlp-3.7.0.jar:stanford-corenlp-3.7.0-models.jar:xom.jar:joda-time.jar:slf4j-api.jar:jollyday.jar -Xmx3g edu.stanford.nlp.pipeline.StanfordCoreNLP -ssplit.eolonly -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file ../knock50_result.txt
