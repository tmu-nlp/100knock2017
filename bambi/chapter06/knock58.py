from bs4 import BeautifulSoup, element
'''
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語(sub)，述語(v?)，目的語の定義は以下を参考にせよ．
述語: nsubj関係とdobj関係の子（dependant）を持つ単語 (つまり、主語と目的語はあいつもつだよね？)
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）
<dep type="nsubj">
  <governor idx="13">enabling</governor>
  <dependent idx="8">understanding</dependent>主語
</dep>
<dep type="dobj">
  <governor idx="13">enabling</governor>
  <dependent idx="14">computers</dependent>目的語
</dep>
'''
class Chunk:
    def __init__(self,g_text,d_text,g_idx,d_idx):
        self.g_text = g_text
        self.d_text = d_text
        self.g_idx = g_idx
        self.d_idx = d_idx
soup = BeautifulSoup(open("nlp.txt.xml"),"lxml")
dependencies = soup.find_all('dependencies',{"type" : "collapsed-dependencies"})
sentences = []
for dependence in dependencies:
    nsubj, dobj = set(), set()
    for child in dependence.children:
        if isinstance(child,element.Tag):
            tag = child["type"]
            governor = child.find("governor")
            dependent = child.find("dependent")
            item = Chunk(governor.text,dependent.text,governor["idx"],dependent["idx"])
            if tag == "nsubj":
                nsubj.add(item)
            elif tag == "dobj":
                dobj.add(item)
    sentences.append([nsubj,dobj])
for s in sentences:
    subjs = s[0]
    objs = s[1]
    for subj in subjs:
        for obj in objs:
            if subj.g_idx == obj.g_idx:
                print("{}\t{}\t{}".format(subj.d_text,subj.g_text,obj.d_text))
