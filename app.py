from flask import Flask, render_template, request, redirect, url_for
from routes import *
from datetime import datetime as dt
from xcelFunc import *
from tables import *

app = Flask(__name__)
my_routes(app)

create_prod_table()
create_model_table()
create_tech_table()
create_costing_table()
create_promo_table()   
create_stk_table()
create_features_table()

if __name__ == '__main__':
    app.run(debug=True)