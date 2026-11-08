
from xcelFunc import read_from_file, margin_calc
#from product import bulkInsert

import pandas as pd

col_Names_1 = ['Sku','Brand', 'Description', 'Cash Price','Year','Average Weighted Cost']
col_Names_2 = ['Sku','Brand', 'Description', 'Cash Price','Year','Stock On Hand','Average Weighted Cost']
searchTerm = 'This Year' 
searchCol = 'Year'

df_1 = read_from_file(r'C:\Users\Vyan\Documents\GitHub\Dashboard\uploads\BSH\BuyerSalesHistory.csv', col_Names=col_Names_1 , searchTerm=searchTerm, searchCol=searchCol, header=None, test=0, n=0)
df_2 = read_from_file(r'C:\Users\Vyan\Documents\GitHub\Dashboard\uploads\Inventory_V.xlsx', col_Names=col_Names_2 , sheet=0,searchTerm=None, searchCol=None, header=None, test=0, n=0)
df_1['Cash_Price'] = df_1['Cash Price'].round(2)
df_1['Stock_On_Hand'] = df_1['Stock On Hand']
df_1['Cost'] = df_1['Average Weighted Cost'].round(2)

df_1['Cash_Price'] = pd.to_numeric(df['Cash Price'], errors='coerce').fillna(0).round(2)
df_1['Cost'] = pd.to_numeric(df_1['Average Weighted Cost'], errors='coerce').fillna(0).round(2)

df_1['Margin'] = df_1.apply(lambda row: margin_calc(row['Cost'],row['Cash_Price']), axis=1).round(2)


data_to_insert = list(df_1[['Sku', 'Description', 'Cash_Price','Cost','Margin','Stock_On_Hand']].itertuples(index=False, name=None))

#print(data_to_insert)
#bulkInsert(data_to_insert)