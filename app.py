from flask import Flask, render_template, request, redirect, url_for
from routes import *
from datetime import datetime as dt
from sqliteDB3 import *
from xcelFunc import *
import locale

app = Flask(__name__)
my_routes(app)
create_table()



if __name__ == '__main__':
    app.run(debug=True)