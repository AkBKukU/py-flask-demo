#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import send_file
from flask import redirect
from flask import make_response

app = Flask("The Reform Script")

@app.after_request
def add_header(r):
    """
    Force the page cache to be reloaded each time
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route("/data.json")
def data_json():
    data={
            "number": 1234,
            "string": "text",
            "float" : 12.34
    }
    return dict(data)


app.run(host="0.0.0.0")
