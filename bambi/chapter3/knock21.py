import json, re
def findTextFromTitle(title):
    with open('jawiki-country.json') as json_data:
        lines = json_data.readlines()
        for line in lines:
            data = json.loads(line)
            if data["title"] == title:
                return data["text"]
def getEnglandArticle():
    return findTextFromTitle("イギリス")
def getCategoryRawList(content):
    return re.findall(r"\[\[Category:.*?\]\]", content)
result = getCategoryRawList(getEnglandArticle())
print("\n".join(result)) #改行したほうが見やすい(result is list)
