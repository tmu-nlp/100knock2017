import pymongo
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def queryArtistName(name, artists):
    artist_list = list()
    for i, artist in enumerate(artists.find({'name':name}).sort('rating.count', -1)):
        artist_info = artist
        artist_list.append(artist_info)
        if i == 50:
            break
    return artist_list

def queryAliasesName(aliases, artists):
    artist_list = list()
    for i, artist in enumerate(artists.find({'aliases.name':aliases}).sort('rating.count', -1)):
        artist_info = artist
        artist_list.append(artist_info)
        if i == 50:
            break
    return artist_list

def queryTags(tag, artists):
    artist_list = list()
    for i, artist in enumerate(artists.find({'tags.value':tag}).sort('rating.count', -1)):
        artist_info = artist
        artist_list.append(artist_info)
        if i == 50:
            break
    return artist_list

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        name = request.form['name']


#        flag_query 0:artist_name
#        flag_query 1:aliase_name
#        flag_query 2:tags

        flag_query = int(request.form['selection'])
        if flag_query == 0:
            ans_artists = queryArtistName(name, artist_co)
        elif flag_query == 1:
            ans_artists = queryAliasesName(name, artist_co)
        elif flag_query == 2:
            ans_artists = queryTags(name, artist_co)
        return render_template('index.html', contents=ans_artists)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client_test_db
    artist_co = db.artists
    app.debug = True
    app.run(host='0.0.0.0')
