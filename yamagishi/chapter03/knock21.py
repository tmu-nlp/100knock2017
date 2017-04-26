from knock20 import getUKdata

for line in getUKdata().split('\n'):
    if 'Category' in line:
        print(line)
