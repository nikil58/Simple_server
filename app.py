import requests
import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["POST","GET", "DELETE"])
def hello_world():
    if request.method == "POST":
        search = request.get_json()
        file=search.get("fileName") +'.txt'
        f = open(file, "w")
        f.write("Hello world")
        f.close()
        return ('check ur folder')
    elif request.method == "DELETE":
        search=request.form.get("Name")
        os.remove(search+'.txt')
        return ('check ur folder')
    elif request.method == "GET":
        search = request.form.get("Name")
        file=search+'.txt'
        f=open(file,'r')
        content=f.read()
        f.close()
        return(content)


if __name__ == '__main__':
    app.run()
