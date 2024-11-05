from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Server is running(-3-)"

def run():
    app.run(host = '0.0.0.0',port = 8000)

def sever_on():
    t = Thread(target=run)
    t.start()