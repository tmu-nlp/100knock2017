from get_chunks_list import get_chunks_list

for c in get_chunks_list()[8+1]:
    print('文節の係り先->'+ str(c.link))
    body = ''
    for mor in c.morphs:
        body += mor.token_body + ' '
    print('文節 -> '+ body)
