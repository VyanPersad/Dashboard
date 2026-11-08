from calendar import Month

from xcelFunc import read_from_file
import pandas as pd
import datetime as dt

def arrival_Log():
    arrival_DF = read_from_file('uploads\\Arriving_Soon.xlsx', test=1, n=0, col_Names = ['STATUS', 'RWT', 'ETA', 'CONTAINER#', 'SUPPLIER', 'DESCRIPTIONS'])
    
    filter_df = arrival_DF[['STATUS', 'RWT', 'ETA', 'CONTAINER#', 'SUPPLIER', 'DESCRIPTIONS']].copy()
    date = pd.to_datetime(filter_df['ETA'], format='%d-%b-%Y',errors='coerce')
    long_date = pd.to_datetime(filter_df['ETA'], format='%d-%b-%Y',errors='coerce').dt.strftime('%Y-%b-%d')
    curr_mon = dt.datetime.now().month
    filter_df['ETA'] = date.dt.date
    filter_df['ETA_2'] = long_date
    filter_df['Month'] = date.dt.month.astype('Int64')
    filter_df['Year'] = date.dt.year.astype('Int64')
    filter_df['Day'] = date.dt.day.astype('Int64')
    filter_df.insert(3, 'ETA_2', filter_df.pop('ETA_2'))

    search_terms = 'TV|SoundBar|Audio|Speaker|Home Theater|Projector|Monitor|Display|Screen|Mini-System'

    max_col_width = 30

    arrival_df = filter_df[
        (filter_df['Year'] >= 2026)
        &
        (filter_df['DESCRIPTIONS'].str.contains(search_terms, case=False, na=False))
        &
        (filter_df['Month'] >= curr_mon-3)
        ].copy()

    arrival_df.loc[:, 'STATUS'] = arrival_df['STATUS'].str.wrap(20)
    arrival_df.loc[:, 'SUPPLIER'] = arrival_df['SUPPLIER'].str.wrap(20)
    arrival_df.loc[:, 'DESCRIPTIONS'] = arrival_df['DESCRIPTIONS'].str.wrap(max_col_width)
    arrival_df = arrival_df.reset_index(drop=True)
    print(arrival_df.to_markdown())
    arrival = arrival_df.sort_values(by='Month', ascending=True)
    print(arrival.to_markdown())
    return arrival
