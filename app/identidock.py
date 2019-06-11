from flask import Flask, Response, request # Response welches Bilder bereitstellt
import requests # dnmonster service 
import hashlib # hash bib einbinden
import redis

app = Flask(__name__)

cache = redis.StrictRedis(host='redis', port=6379, db=0)
salt = "UNIQUE_SALT" # Salt var anlegen
default_name = 'lucas lutze'

@app.route('/', methods=['GET', 'POST']) #standart nur Get Post muss explizit hinzugefügt werden
def mainpage():

    name = default_name
    if request.method == 'POST': # Funktionalität für den Button
        name = request.form['name']

    salted_name = salt + name #"rnd" wert mit namen addieren
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest() #hashen und als hexa wert abspeichern

    header = '<html><head><title>Identidock</title></head><body>'
    body = '''<form method="POST">
              Hallo <input type="text" name="name" value="{}">
              <input type="submit" value="abschicken">
              </form>
              <p>Du siehst aus wie ein:
              <img src="/monster/monster.png"/>
              '''.format(name, name_hash)
    footer = '</body></html>'

    return header + body + footer

@app.route('/monster/<name>')
def get_identicon(name):

    image = cache.get(name)
    if image is None:  # vergleicht ob bild im cache
        print ("Cache miss", flush=True)
        r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
        image = r.content
        cache.set(name, image)

    return Response(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
