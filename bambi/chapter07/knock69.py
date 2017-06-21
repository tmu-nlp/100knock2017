from flask import Flask, render_template, request, url_for
from pymongo import MongoClient
from app import app

client = MongoClient()
db = client.knock
collection = db.artist

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',
                            title="title")

@app.route('/post', methods=['GET', 'POST'])
def post():
    tag=request.form['tag']
    items = [x for x in collection.find({"tags.value": tag})]
    result = []
    for x in items:
        if "rating" in x:
            result.append((x["name"], x["rating"]["value"]))
    answer = sorted(result,key=lambda x:x[1], reverse=True)

    return render_template('post.html', items=answer)
