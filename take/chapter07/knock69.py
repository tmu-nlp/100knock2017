from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

from pymongo import MongoClient, DESCENDING, ASCENDING

client = MongoClient('localhost', 27017)
db = client.DB_NAME
cl = db.sample

cl.create_index([("name", ASCENDING), ("aliases[].name", ASCENDING)])
cl.create_index([("tag", ASCENDING), ("tags[].value", ASCENDING)])
cl.create_index([("rating.count", DESCENDING)])

@app.route('/')
def index():
    return render_template('index.html',title="helloworld")

@app.route('/sendquery', methods=['POST'])
def sendtext():
    _name = request.form['name']
    _alias = request.form['alias']
    _tag = request.form['tag']
    _limit = request.form['limit']
    print('{} {} {} {}'.format(_name, _alias, _tag, _limit))
    print("type(limit) {}".format(type(_limit)))

    if len(str(_limit)) < 1:
        _limit = 10
        print("limit force to 10")
    elif int(_limit) <= 0 or int(_limit) > 200:
        print("limit force to 10")
        _limit = 10
    else:
        _limit = int(_limit)

    query_dict = dict()
    if len(_name) > 0:
        query_dict['name'] = _name

    if len(_alias) > 0:
        query_dict['aliases.name'] = _alias

    if len(_tag) > 0:
        query_dict['tags.value'] = _tag

    print(str(query_dict))
    name_list = list()
    # for out in cl.find({'tags.value':_tag, 'name':_name, 'aliases.name':_alias}).sort('rating.count', DESCENDING).limit(_limit):
    for out in cl.find(query_dict).sort('rating.count', DESCENDING).limit(_limit):
        print(out.get('name'))
        name_list.append(out.get('name'))
    return render_template('index.html', name=name_list)

if __name__ == "__main__":
   app.run()
