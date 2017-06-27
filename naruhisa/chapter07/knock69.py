from flask import Flask, render_template, request, request, redirect, url_for
import pymongo
import webbrowser

app = Flask(__name__)

def search_artist(txt):
    client = pymongo.MongoClient()
    db = client.MusicBrainz_DB
    collection = db.artist_collection

    results = []
    for each_artist in collection.find({"tags.value": txt}).sort('rating.count', -1).limit(10):
        result = []
        for key, value in sorted(each_artist.items()):
            if key == 'name':
                result.append('{}   :   {}'.format(key, value))
        results.append(result)
    if txt == '嶋中に感謝':
        results = 'わかる'
    elif txt == 'Suganさんに感謝':
        results = '感謝'
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        search_txt = request.form['txt']
        results = search_artist(search_txt)
        if results == []:
            results = '誰やねん'

        return render_template('index.html', results=results)
    else:
        return redirect(url_for('index'))

if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/', new=1, autoraise=True)
    app.debug = True
    app.run()
