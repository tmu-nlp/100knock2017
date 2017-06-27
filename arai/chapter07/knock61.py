import  plyvel
import sys

my_db = plyvel.DB('artist.db', create_if_missing = True)
argvs = sys.argv[1]
    #print(j_f)
area = my_db.get(argvs.encode('utf-8'))
print(area)
my_db.close()

#my_db = plyvel.DB()
