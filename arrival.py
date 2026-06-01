from calendar import Month

from xcelFunc import read_from_file
import pandas as pd
import datetime as dt

def arrival_Log():
    arrival_DF = read_from_file('uploads\\Arriving_Soon.xlsx', test=1, n=0, col_Names = ['STATUS', 'RWT', 'ETA', 'CONTAINER#', 'SUPPLIER', 'DESCRIPTIONS'])
    
    date = pd.to_datetime(arrival_DF['ETA'], errors='coerce')

    arrival_DF['ETA'] = date.dt.date
    arrival_DF['Month'] = date.dt.month.astype('Int64')
    arrival_DF['Year'] = date.dt.year.astype('Int64')

    search_terms = 'TV|SoundBar|Audio|Speaker|Home Theater|Projector|Monitor|Display|Screen|Mini-System'

    arrival = arrival_DF[
        (arrival_DF['Year'] >= 2026)
        &
        (arrival_DF['DESCRIPTIONS'].str.contains(search_terms, case=False, na=False))
        ]
    
    arrival = arrival.sort_values(by='Month', ascending=True)
    return arrival