import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def read_from_file(filepath, test=0, n=5, header=None, col_Names = [], sheet = 0, searchTerm=None, searchCol=None):
    filetype = filepath.split('.')[1]
    #This will read the csv and display the first 5 rows of the data.
    if (filetype == 'csv'):
        if (col_Names == []):
            dataFrame = pd.read_csv(filepath)
            #dataFrame = pd.read_csv(filepath, sep=';')
            #In the abobve line we tell python to use the ; as the spearator.
            if (test == 0):
                print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
            elif (test == 1):
                print(dataFrame.head(n))
        elif (col_Names != []):
            dataFrame = pd.read_csv(filepath)
            dataFrame = dataFrame[dataFrame[searchCol]==searchTerm]
            dataFrame = dataFrame[col_Names]
            #dataFrame = pd.read_csv(filepath, sep=';')
            #In the abobve line we tell python to use the ; as the spearator.
            if (test == 0):
                print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the number of rows.')
            elif (test == 1):
                print(dataFrame.head(n))

        return dataFrame

    elif (filetype == 'xlsx'):
        xlFile = pd.ExcelFile(filepath)  
        sheetName = xlFile.sheet_names[sheet]
        dataFrame = xlFile.parse(f'{sheetName}')
        if (test == 0):
            print('Set test to 1 to view sample datraframes, Default is the first 5 rows, set n to vary the numbe rof rows.')
        elif (test == 1):
            print(dataFrame.head(n))

        return dataFrame
    
def readCols(dataFrame, colName1, colName2, colName3):
    dF = dataFrame[[colName1, colName2, colName3]]
    return dF

def search_DF(dataFrame, searchTerm):
    df = dataFrame[dataFrame['Sku'] == searchTerm]
    return df

def linePlot(dataFrame, searchTerm, title='None', xlabel='X-Axis', ylabel='Y-Axis', xloc=1.10, yloc=0.5):   
    thisYear = dataFrame[dataFrame['Year'] == 'This Year']
    selectSKU = thisYear[thisYear['Sku'] == searchTerm]
    all_month_names = ['April', 'May', 'June','July', 'August', 'September', 
                       'October', 'November', 'December','January', 'February', 'March']
    month_abbr = ['Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 
                  'Oct', 'Nov', 'Dec','Jan', 'Feb', 'Mar']
    selectSKU = selectSKU.set_index('Sku')
    selectSKU = selectSKU.T
    selectSKU = selectSKU[selectSKU.index.isin(all_month_names)]
    #print(selectSKU)
    plt.plot(selectSKU.index, selectSKU[searchTerm], marker='', label='')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.xticks(ticks=all_month_names, labels=month_abbr)
    plt.ylabel(ylabel)
    plt.legend(loc = (xloc, yloc))
    plt.tight_layout()
    plt.savefig('static/Test_Sales.png')

    plt.close()

def margin_calc(cost, price , vat=0.125):
    if cost == 0 or price == 0 or cost ==None or price == None:
        return 0    
    else :
        margin = (((price)/(1 + vat)) - cost) / ((price/(1 + vat))) * 100
    return margin