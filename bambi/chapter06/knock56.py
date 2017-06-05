'''
tag名だけで変えてもいいよね？？
ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．→何を言いたい！？
もしかして:
<mention> -> <mention representative="false"> 欲しい??「元の参照表現が分かる」とは <mention representative="true">　と区割りできればいいよね？
'''
from bs4 import BeautifulSoup, element
soup = BeautifulSoup(open("nlp.txt.xml"),"lxml")
mentions = soup.find_all('mention')
'''
      <coreference>
        <mention representative="true">
          <sentence>1</sentence>
          <start>33</start>
          <end>34</end>
          <head>33</head>
          <text>computers</text>
        </mention>
        <mention>
          <sentence>3</sentence>
          <start>14</start>
          <end>15</end>
          <head>14</head>
          <text>computers</text>
        </mention>
      </coreference>
'''
for m in mentions:
    if m.has_attr('representative') == False:
        print("before: =>\n{}".format(m))
        # add new attribute
        m["representative"] = "false"
        print("after: =>\n{}".format(m))
