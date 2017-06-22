'''
Usage:
$ python knock61.py who1 who2...
'''

import redis
import sys

args = sys.argv

r = redis.Redis()
for who in args[1:]:
    areas = r.smembers(who)
    if len(areas) > 0:
        print('{}\t{}'.format(who,areas))
    else:
        print("{}\tNO DATA".format(who))

