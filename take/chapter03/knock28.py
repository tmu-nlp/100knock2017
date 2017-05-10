import re
from knock20 import gen_uk_info

m = re.findall(r'{{2}基礎情報([\s\S]+?)\n}{2}', gen_uk_info())
for i in m:
    result_dict   = re.findall(r'\n|(.*?)\s=\s(.*?)\n\|', i, flags=re.M|re.S)
    for k,v in result_dict:
        m26 = re.sub(r"\'{2,5}", '', v)
        m27 = re.sub(r'\[{2}([^#|\]]+?)\]{2}|\[{2}([^#|\]]+?)[|#].+?\]{2}', '\\1\\2', m26)
        rm_html_tag = re.sub(r'<.*?>', '', m27)
        rm_lang_info = re.sub(r'{{2}lang*\|[\s\S]+?\|([\s\S]+?)}{2}', '\\1', rm_html_tag)
        print('after remove lang info:{} : {}'.format(k,rm_lang_info))
        rm_ext_link = re.sub(r'\[http.+?\]$', '', rm_lang_info)
        print('after remove ext link :{} : {}'.format(k, rm_ext_link))
