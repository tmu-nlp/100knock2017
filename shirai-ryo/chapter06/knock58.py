"""

Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

述語: nsubj関係とdobj関係の子（dependant）を持つ単語
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）

"""

"""
なんか公式のやつ

for neighbor in root.iter('neighbor'):
...     print(neighbor.attrib)
...
{'name': 'Austria', 'direction': 'E'}
{'name': 'Switzerland', 'direction': 'W'}
{'name': 'Malaysia', 'direction': 'N'}
{'name': 'Costa Rica', 'direction': 'W'}
{'name': 'Colombia', 'direction': 'E'}

Element.iter() などの、配下 (その子ノードや孫ノードなど) の部分木全体を再帰的にイテレートするいくつかの役立つメソッドを持っています
atttribはよくわからん
"""



import xml.etree.ElementTree as ET
with open("nlp.txt.xml") as input_text:
    tree = ET.parse(input_text)
    root = tree.getroot()

# <governor> が係り元、 <dependent> が係り先
    for d in root.iter("dependencies[@type = 'collapsed-dependencies']/dep"):
        v_nsub = ""
        v_dobj = ""
        s = ""
        o = ""
        if dep.get("type") == "nsubj" :
            v_nsub = dep.find("governor").text
            s = dep.find("dependent").text
        elif dep.get("type") == "vdobj":
            v_dobj = dep.find("governor").text
            o = dep.find("dependent").text
                #print(v_nsub, v_dobj, s, o)

        if v_nsub == v_dobj: #主語、述語、目的語が一致してるかどうか
                print("{}\t{}\t{}".format(s, v_nsub, o))
