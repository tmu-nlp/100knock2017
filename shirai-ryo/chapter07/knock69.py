import sys
from pymongo import MongoClient, ASCENDING, DESCENDING
from bottle import route, run, template, request

client = MongoClient('localhost', 27017)
db = client.my_database
co = db.my_collection


@route('/')
def dicroot():
    query_tag = ['name', 'aliases.name', 'tags.value']
    query_dict = dict()
    query_list = [request.query.name, request.query.aliases_name, request.query.tags_name]
    for tag, query in zip(query_tag, query_list):
        if query:
            query_dict[tag] = query
    if query_dict:
        result = co.find(query_dict)
    else:
        result = [{}]
    print(list(co.find(query_dict)[:10]))
    answer = list()
    search_result = list()
    return template("root", result = result, query = query_dict)



if __name__ == '__main__':
    run(host = 'localhost', port = 8080, debug = True, reloader = True)
