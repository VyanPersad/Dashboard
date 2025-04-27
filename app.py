from flask import Flask, render_template, request
from datetime import datetime as dt
from sqliteDB3 import *

app = Flask(__name__)
create_table()

@app.route('/', methods=['GET', 'POST'])
def home():
    year = dt.now().year
    day = dt.now().day 
    month = dt.strftime(dt.now(),'%B')
    if request.method == 'POST':
        if request.form.get("addButton")=="Add":
            code = request.form.get("addCode")
            model = request.form.get("addModel")
            price = request.form.get("addPrice")
            print(f"Code: {code}, Model: {model}, Price: {price}")
            insert(code, model, price)
            print("Data Inserted") 
            
        elif request.form.get("delAllButton")=="Delete All":
            deleteAll()
            
        elif request.form.get("delButton")=="Delete":
            code = request.form.get("delCode")
            delete(code)
            
        elif request.form.get("updateButton")=="Update":
            code = request.form.get("upCode")
            model = request.form.get("upModel")
            price = request.form.get("upPrice")
            print(f"Code: {code}, Model: {model}, Price: {price}")
            update(code, model, price)
            print("Data Updated") 

    rows = viewAll()
    
    search_term = None
    if request.method == 'POST':
        if request.form.get("serButton")=="Search":
            search_term = request.form.get("serCode")
            print(f"Search Term: {search_term}")
    searchs = searchDB(search_term)

    return render_template('index.html', year=year, day=day, month=month, rows=rows, searchs=searchs) 

if __name__ == '__main__':
    app.run(debug=True)