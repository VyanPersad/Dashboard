from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime as dt
from sqliteDB3 import *
from xcelFunc import *
import locale

app = Flask(__name__)
create_table()

@app.route('/', methods=['GET', 'POST'])
def home():
    search_term = None
    year = dt.now().year
    day = dt.now().day 
    month = dt.strftime(dt.now(),'%B')
    if request.method == 'POST':
        if request.form.get("addButton")=="Add":
            code = request.form.get("addCode")
            model = request.form.get("addModel")
            price = request.form.get("addPrice")
            #print(f"Code: {code}, Model: {model}, Price: {price}")
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

        elif request.form.get("serButton")=="Search":
            search_term = request.form.get("serCode")
            print(f"Search Term: {search_term}")    

        elif request.form.get("goToButton")=="Go To":
             print("Going to viewEntries")
             return redirect(url_for('viewEntries'))
        
    rows = viewAll()
    searchs = searchDB(search_term)  

    return render_template('index.html', year=year, day=day, month=month, rows=rows, searchs=searchs) 

@app.route('/viewEntries', methods=['GET', 'POST'])
def viewEntries():
    search_term = None

    mainDF= read_from_file('resources\\BuyerSalesHistory.csv', test=1, n=0, col_Names = ['Sku','Brand', 'Description', 'Cash_Price'], searchCol='Year', searchTerm='This Year')
    mainDF['Cash_Price'] = mainDF['Cash_Price'].round(2).apply(lambda x: f'{x:.2f}')
    outputs = mainDF.to_dict(orient='records')
    
    if request.method == 'POST':
        if request.form.get("serButton")=="Search":
            search_term = request.form.get("serCode")
            print(f"Search Term: {search_term}")  

        elif request.form.get("goToButton")=="Go To":
             print("Going to home")
             return redirect(url_for('home'))      
            
    rows = viewAll()
    searchs = searchDB(search_term)
    return render_template('viewEntries.html', rows=rows, searchs=searchs, outputs=outputs)

if __name__ == '__main__':
    app.run(debug=True)