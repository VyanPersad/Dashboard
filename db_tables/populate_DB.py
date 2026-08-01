from turtle import pd

from xcelFunc import read_from_file, margin_calc
from product import bulkInsert

import pandas as pd

col_Names = ['Sku','Brand', 'Description', 'Cash Price','Year','Stock On Hand','Average Weighted Cost']
searchTerm = 'This Year' 
searchCol = 'Year'

df = read_from_file(r'C:\Users\Vyan\Documents\GitHub\Dashboard\uploads\BSH\BuyerSalesHistory.csv', col_Names=col_Names , searchTerm=searchTerm, searchCol=searchCol, header=None, test=0, n=0)
df['Cash_Price'] = df['Cash Price'].round(2)
df['Stock_On_Hand'] = df['Stock On Hand']
df['Cost'] = df['Average Weighted Cost'].round(2)

df['Cash_Price'] = pd.to_numeric(df['Cash Price'], errors='coerce').fillna(0).round(2)
df['Cost'] = pd.to_numeric(df['Average Weighted Cost'], errors='coerce').fillna(0).round(2)

df['Margin'] = df.apply(lambda row: margin_calc(row['Cost'],row['Cash_Price']), axis=1).round(2)
#print(df['Margin'])
#print(df['Stock_On_Hand'])
data_to_insert = list(df[['Sku', 'Description', 'Cash_Price','Cost','Margin','Stock_On_Hand']].itertuples(index=False, name=None))

bulkInsert(data_to_insert)