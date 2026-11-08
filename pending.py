from xcelFunc import read_from_file_2 
from datetime import datetime as dt
import pandas as pd

def pending_File():

    this_yr = dt.now().year
    curr_mon = dt.now().month
    last_mon = curr_mon - 4
    next_mon = curr_mon + 1
    print(curr_mon, last_mon, next_mon)

    try:
        df = read_from_file_2('uploads\\PO_Pending\\Reportes Courts.xlsx', test=1, n=0)

    except Exception as e: 
        arrival_list = []  
        return arrival_list
   
    major_Filter = df[
        (df['Division'].str.contains('VIDEO', na=False)) |
        (df['Division'].str.contains('AUDIO', na=False)) |
        (df['Division'].str.contains('GAMING', na=False))]

    grouped_df = major_Filter[['Class', 'Division','Brand', 'Code Courts', 'Model','Description','PO','Expected Delivery Date','Pending']].copy()
    grouped_df['Brand'] = grouped_df['Brand'].str.split(" ",n=2).str[2]
    grouped_df['Expected Delivery Date'] = pd.to_datetime(grouped_df['Expected Delivery Date'], format='%d-%b-%Y',errors='coerce')
    grouped_df['Pending'] = grouped_df['Pending'].round(0).astype('Int64') 
    grouped_df['PO'] = grouped_df['PO'].round(0).astype('Int64') 

    date_df = grouped_df[
        (grouped_df['Expected Delivery Date'].dt.year == this_yr)
        &
        (grouped_df['Expected Delivery Date'].dt.month >= last_mon)
        ]

    print(date_df)
    date_df = date_df.sort_values(by='Expected Delivery Date', ascending=True).reset_index(drop=True)
    
    arrival_list = date_df.to_dict(orient='records')
    
    return arrival_list