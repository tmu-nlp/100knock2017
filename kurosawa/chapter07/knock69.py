# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import pymongo
from knock65 import conect_db
import re
import webbrowser

app = Flask(__name__)

# Routing
@app.route('/')
def index():
    title = "artist serch"
    return render_template('index.html', title=title)

@app.route('/post', methods=['POST', 'GET'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        co = conect_db()
        name = request.form['name']
        name = re.compile('.*{0}.*'.format(name))
        result = []
        if not(request.form['name']):
            return render_template('index.html')
        for i,data in enumerate(co.find({'$or':[{'name':name},{'area':name},{'aliases.name':name},{'tags.value':name}]}, sort = [('rating.count',pymongo.DESCENDING),('rating.value',pymongo.DESCENDING)])):
            if i <100:
                result.append(data)
            else:
                i = 99
                break
        return render_template('index.html', result=result, title=title, name=request.form['name'],num=i+1)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/',new=1,autoraise=True)
    app.run()
