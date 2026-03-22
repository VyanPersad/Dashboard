from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime as dt
from sqliteDB3 import *
from viewEntries import viewEntries_File
from xcelFunc import *

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
        #print(rows)
        searchs = searchDB(search_term)  

        return render_template('index.html', year=year, day=day, month=month, rows=rows, searchs=searchs) 

    @app.route('/uploadFile', methods=['GET', 'POST'])
    def uploadFile():
        year, day, month = date_File()
        file_List = upload_File()
        return render_template('uploadFile.html', year=year, day=day, month=month, fileList=file_List)

    @app.route('/deleteFile/<file_Name>', methods=['POST'])
    def deleteFile(file_Name):
        delete_File(file_Name)
        return redirect(url_for('uploadFile'))

    @app.route('/viewEntries', methods=['GET', 'POST'])
    def viewEntries():
        searches, outputs, months, data = viewEntries_File()

        rows = viewAll()

        return render_template('viewEntries.html', rows=rows, searches=searches, outputs=outputs, months=months, chart_labels = months, chart_data = data)
        
    @app.route('/layout', methods=['GET', 'POST'])
    def viewLayout():
        if request.method == 'POST':
            if request.form.get("goToButton")=="Go To View":
                return redirect(url_for('home'))

        return render_template('viewLayout.html')
