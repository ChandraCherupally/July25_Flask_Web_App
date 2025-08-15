from flask import Flask

app = Flask(__name__)

@app.route(rule="/Naveen",methods=["GET"])
def hello_world():
    return "<p>Hello, Naveen!</p>"

@app.route(rule="/Ping",methods=["GET"])
def pinger():
    return {'message': 'Hi, Naveen!'}
