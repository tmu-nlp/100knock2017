from knock20 import jsonget
en = jsonget().split('\n')
for data in en:
    if 'Category' in data:
        print(data)
