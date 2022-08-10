import os

import requests
import json
from flask import Flask, request, json

app = Flask(__name__)

fpath = C:\Users\kunal.nagpure\PycharmProjects\flaskapp\personal.json
@app.route("/")

def home():
    response = requests.post('https://httpbin.org/post', json={'id': 1, 'name': 'Kunal'})
    FileCheck(personal.json)

def FileCheck(name):
    if os.path.isfile(fpath) and os.access(fpath, os.W_OK):
        # checks if file exists
        print ("File exists and is writable")
    else:
        return "400"
def Writetofile(data):
    with open(os.path.join(fpath, 'personal.json'), 'w+') as file:
        file.write(json.dumps())

@app.route("/Kunal")
def Kunal():
    return "Hello, Kunal"


if __name__ == "__main__":
    app.run(debug=True)