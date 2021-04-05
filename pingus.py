from threading import Thread
from flask import Flask
import datetime

app = Flask('')

@app.route('/')
def home():
    return """Latest ping: {}""".format(datetime.datetime.now().strftime('%b %d, %Y | %I:%M:%S %p UTC'))

def run():
    app.run(host='0.0.0.0',port=8080)

def up():
    t = Thread(target=run)
    t.start()