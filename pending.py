from flask import redirect, redirect, request, url_for
from xcelFunc import *
from datetime import datetime as dt
import pandas as pd

def arrival_File():

    try:
       poDF = read_from_file('uploads\\PO_Pending\\Reportes Courts.xlsx', test=1, n=0, col_Names = ['Brand','Division','Model','Description','Expected Delivery Date'])

    except Exception as e: 
        arrival_list = []  
        return arrival_list
    
    poDF = poDF[
        (poDF['Division'].str.contains('VISION'))|
        (poDF['Division'].str.contains('AUDIO'))
    ]

    poDF['Brand'] = poDF['Brand'].str.split(" ",n=2, expand=True)[2]
    poDF['Expected Delivery Date'] = pd.to_datetime(poDF['Expected Delivery Date'])
    poDF = poDF.sort_values(by='Expected Delivery Date', ascending=True)
    poDF['Expected Delivery Date'] = poDF['Expected Delivery Date'].dt.strftime('%A, %d %B %Y')
    arrival_list = poDF.to_dict(orient='records')
    return arrival_list