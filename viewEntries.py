from flask import redirect, redirect, request, url_for
from xcelFunc import *

def viewEntries_File():
    search_term = []
    searches = []
    data = []
    mainDF = read_from_file('resources\\BuyerSalesHistory.csv', test=1, n=0, col_Names = ['Sku','Brand', 'Description', 'Cash Price','Year',
    'April','May','June','July','August','September','October','November','December','January','February','March'], 
    searchCol='Year', searchTerm='This Year')
    mainDF = mainDF[mainDF['Year'] == 'This Year']
    mainDF['Cash Price'] = mainDF['Cash Price'].round(2).apply(lambda x: f'{x:.2f}')
    mainDF['Description'] = mainDF['Description'].str.split('- ').str[1] 
    months = ['April', 'May', 'June', 
                  'July', 'August', 'September',
                  'October', 'November', 'December', 
                  'January', 'February', 'March']        
    outputs = mainDF.to_dict(orient='records')        

    if request.method == 'POST':

        if request.form.get("serButton")=="Search":
            search_term = request.form.get("serCode")
            searches = search_DF(mainDF, search_term)

            if searches.empty:
                searches = []
                data = [0 for m in months]
            else:
                results = searches.to_dict(orient='records')
                results = results[0]
                #linePlot(mainDF, searchTerm=search_term, title='Sales', xlabel='Month', ylabel='Sales', xloc=1.10, yloc=0.5)
                data = [results[m] for m in months]

        elif request.form.get("goToButton")=="Go To":
            print("Going to home")
            return "REDIRECT", None ,None, None   

    return searches, outputs, months, data   
        
    