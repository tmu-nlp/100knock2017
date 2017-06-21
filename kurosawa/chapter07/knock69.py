from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods = ['GET','POST'])
def post():
    name = request.for['name']

