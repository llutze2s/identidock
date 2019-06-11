from flask import Flask, Response, request # Response welches Bilder bereitstellt
import html
import platform

app = Flask(__name__)

@app.route('/')
def mainpage():

    header = '<html><head><title>Identidock</title></head><body>'
    body = '''<form method="GET">
              CPU = {{platform.machine()}}
              Prozessor = {{platform.processor()}}
              System = {{platform.system}}
              System version = {{platform.version()}}
              '''.format(name, name_hash)
    footer = '</body></html>'

    return header + body + footer

if __name__ == '__main__':
    app.run(host='0.0.0.0')
