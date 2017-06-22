import plyvel
import sys

kensaku = plyvel.DB('./kn60.ldb/',create_if_missing=True)
print(kensaku.get(sys.argv[1].encode('utf-8')))
