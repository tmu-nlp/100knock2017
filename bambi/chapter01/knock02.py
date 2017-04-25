zipped = zip(list("パトカー"),list("タクシー")) # https://docs.python.org/3/library/functions.html#zip
content = list(zipped)
result = "".join(["".join(pair) for pair in content])
print(str(result))
