import xml.etree.ElementTree as ET

def make_corenlp_SVO(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    for dependencies in root.findall(".//dependencies[@type='collapsed-dependencies']"):
        for dep_nsubj in dependencies.findall(".//dep[@type='nsubj']"):
            for dep_dobj in dependencies.findall(".//dep[@type='dobj']"):
                if dep_nsubj[0].get('idx') == dep_dobj[0].get('idx'):
                    print('\t'.join([dep_nsubj[1].text, dep_nsubj[0].text, dep_dobj[1].text]), file=data_out)

if __name__ == '__main__':
    with open('knock58_result.txt', 'w') as data_out:
        data_in_path = '../data/knock50_result.txt.xml'
        make_corenlp_SVO(data_in_path, data_out)

# XML Parserでの基本的なメソッドはドキュメントを参照。今回用いた、XPath構文は次のように用いる。root.findall("")の中身のpathは、.//〜 で〜に一致するすべての子要素を選択。[@type='〜']とすることにより〜の属性を持つ子要素を選択することができる。
