purge_token_list = ['.', ',', '!', '?', ';', ':', '(', ')', '[', ']', '"']
inputfile = 'enwiki-20150112-400-r100-10576.txt'
#inputfile = 'mini.txt'
purged_file = 'purged.txt'

with open(inputfile) as f, open(purged_file, 'w') as out_f:
    for line in f:
        words = line.strip().split()
        purged_line = []
        for word in words:
            purge_head = word[0] in purge_token_list
            purge_end = word[-1] in purge_token_list
            
            if not purge_head and not purge_end:
                purged_line.append(word)
                continue
            elif purge_head and purge_end:
                #頭、末どっちもpurge
                t = word[1:-1]
                # purged_line.append(word[1:-1])
            elif purge_head and not purge_end:
                # 頭だけpurge
                t = word[1:]
                # purged_line.append(word[1:])
            elif not purge_head and purge_end:
                # 末だけpurge
                t = word[:-1]
                # purged_line.append(word[:-1])
            else:
                pass
            if len(t) > 0:
                purged_line.append(t)
        print(' '.join(purged_line), file=out_f)
