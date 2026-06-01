from flask import Flask, render_template, request, redirect, url_for
from routes import *
from datetime import datetime as dt
from xcelFunc import *

app = Flask(__name__)
my_routes(app)

if __name__ == '__main__':
    app.run(debug=True)