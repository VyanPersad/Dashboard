from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime as dt
from sqliteDB3 import *
from xcelFunc import *


def my_routes(app):
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
                return redirect(url_for('home')) 
                
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
                return redirect(url_for('home'))

            elif request.form.get("serButton")=="Search":
                search_term = request.form.get("serCode")
                print(f"Search Term: {search_term}")    

            elif request.form.get("clearButton")=="Clear All":
                search_term = " "
                print(f"Search Term: {search_term}")  

            elif request.form.get("goToButton")=="Go To":
                print("Going to viewEntries")
                return redirect(url_for('viewEntries'))
            
            elif request.form.get("goToButton")=="Go To View":
                print("Going to viewLayout")
                return redirect(url_for('viewLayout'))
        rows = viewAll()
        searchs = searchDB(search_term)  

        return render_template('index.html', year=year, day=day, month=month, rows=rows, searchs=searchs) 

    @app.route('/viewEntries', methods=['GET', 'POST'])
    def viewEntries():
        search_term = []
        searches = []
        mainDF= read_from_file('resources\\BuyerSalesHistory.csv', test=1, n=0, col_Names = ['Sku','Brand', 'Description', 'Cash Price','Year',
        'April','May','June','July','August','September','October','November','December','January','February','March'], 
        searchCol='Year', searchTerm='This Year')
        mainDF['Cash Price'] = mainDF['Cash Price'].round(2).apply(lambda x: f'{x:.2f}')
        mainDF['Description'] = mainDF['Description'].str.split('- ').str[1] 
        months = ['April', 'May', 'June', 
                  'July', 'August', 'September',
                  'October', 'November', 'December', 
                  'January', 'February', 'March']        
        outputs = mainDF.to_dict(orient='records')
        #print(outputs)
        if request.method == 'POST':
            if request.form.get("serButton")=="Search":
                search_term = request.form.get("serCode")
                searches = search_DF(mainDF, search_term).to_dict(orient='records')
                #print(searches)
                linePlot(mainDF, searchTerm=search_term, title='Sales', xlabel='Month', ylabel='Sales', xloc=1.10, yloc=0.5)
                results = searches[0]
                data = [results[m] for m in months]
                #print(data)
                #print(f"Search Term: {search_term}")  

            elif request.form.get("goToButton")=="Go To":
                print("Going to home")
                return redirect(url_for('home'))      
                
        rows = viewAll()
        #searchs = searchDB(search_term)
        return render_template('viewEntries.html', rows=rows, searches=searches, outputs=outputs, months=months, chart_labels = months, chart_data = data)
        #return render_template('viewEntries.html', outputs=outputs)
        
    @app.route('/layout', methods=['GET', 'POST'])
    def viewLayout():
        if request.method == 'POST':
            if request.form.get("goToButton")=="Go To View":
                return redirect(url_for('home'))

        return render_template('viewLayout.html')
