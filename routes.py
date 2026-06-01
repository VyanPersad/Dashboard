from flask import render_template, request, redirect, url_for
from datetime import datetime as dt

from pandas import test
from arrival import arrival_Log

from viewEntries import viewEntries_File
from pending import arrival_File
from xcelFunc import *
from db_tables.product import *

from upload import upload_File, delete_File
from date import date_File


def my_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        year, day, month = date_File()
        if request.method == 'POST':
            if request.form.get("goToUpload")=="Go To Upload":
                return redirect(url_for('uploadFile'))
            
            elif request.form.get("goToIndex")=="Go To Index":
                return redirect(url_for('index'))
            
            elif request.form.get("goToEntries")=="Go To Entries":
                return redirect(url_for('viewEntries'))
            
            elif request.form.get("goToPo")=="Go To PO Pending":
                return redirect(url_for('arrivals'))
            
            elif request.form.get("goToLog")=="Go To Arrival Log":
                return redirect(url_for('arrival_log'))
            
            year, day, month = date_File()
        return render_template('home.html', year=year, day=day, month=month) 

    @app.route('/index', methods=['GET', 'POST'])
    def index():
        search_term = None
        year = dt.now().year
        day = dt.now().day 
        month = dt.strftime(dt.now(),'%B')
        if request.method == 'POST':
            if request.form.get("addButton")=="Add":
                code = request.form.get("addCode")
                model = request.form.get("addModel")
                price = request.form.get("addPrice")
                insert(code, model, price)
                print("Data Inserted")
                return redirect(url_for('index')) 
                
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
                return redirect(url_for('index'))

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

    @app.route('/uploadFile', methods=['GET', 'POST'])
    def uploadFile():
        year, day, month = date_File()
        bsh_List, pop_List, aged_List = upload_File()
        return render_template('uploadFile.html', year=year, day=day, month=month, bsh_List=bsh_List, pop_List=pop_List, aged_List=aged_List)

    @app.route('/deleteFile/<folder>/<file_Name>', methods=['POST','GET'])
    def deleteFile(folder,file_Name):
        delete_File(folder, file_Name)
        return redirect(url_for('uploadFile'))

    @app.route('/viewEntries', methods=['GET', 'POST'])
    def viewEntries():
        
        result = viewEntries_File()

        if result[0] == "REDIRECT":
            return redirect(url_for('home'))
        
        searches, outputs, months, data = viewEntries_File()

        return render_template('viewEntries.html', rows=searches, searches=searches, outputs=outputs, months=months, chart_labels = months, chart_data = data)
        
    @app.route('/layout', methods=['GET', 'POST'])
    def viewLayout():
        if request.method == 'POST':
            if request.form.get("goToButton")=="Go To View":
                return redirect(url_for('home'))

        return render_template('viewLayout.html')

    @app.route('/arrivals', methods=['GET', 'POST'])
    def arrivals():
        if request.method == 'POST':
            if request.form.get("goToHome")=="Go To Home":
                return redirect(url_for('home'))

        containers = arrival_File()

        return render_template('arrival.html', containers=containers)
    
    @app.route('/arrival_log', methods=['GET', 'POST'])
    def arrival_log():
        if request.method == 'POST':
            if request.form.get("goToHome")=="Go To Home":
                return redirect(url_for('home'))

        arrival = arrival_Log()

        return render_template('arrival_log.html', containers=arrival.to_dict(orient='records'))