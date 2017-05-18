
# coding: utf-8

# In[6]:

#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import sys, pprint, re,requests,json


# In[82]:

sec=re.compile("\{\{基礎情報 国.+?\n\}\}\n",flags=re.DOTALL)
key_value=re.compile("^\|(.+?) = (.+?)\n(?=\|)",flags=re.DOTALL|re.MULTILINE)
inner_link=re.compile("\[\[(.+?)\]\]")


# In[44]:

with open("./UK.txt","r") as f:
    lines=f.read()


# In[79]:

match=sec.findall(lines)
dict_items=key_value.findall(match[0])
dict={i:j for i, j in dict_items}


def get_response(name):
    end_point = 'https://en.wikipedia.org/w/api.php'
    params = {'action': 'query', 'format': 'json', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': 'File:{}'.format(name)}
    response = requests.get(end_point, params)
    return response.json()

json_image_str=get_response(dict["国旗画像"])

pprint.pprint(json_image_str['query']['pages']['23473560']['imageinfo'][0]['url'])




