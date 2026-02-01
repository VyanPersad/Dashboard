from xcelFunc import read_from_file, margin_calc
from sqliteDB3 import insert, bulkInsert


df = read_from_file('resources\\BuyerSalesHistory.csv', test=0, n=0, 
                    col_Names = ['Sku','Brand', 'Description', 'Cash Price','Year','Stock On Hand','Average Weighted Cost'], searchTerm='This Year', searchCol='Year')
df['Cash_Price'] = df['Cash Price'].round(2)
df['Stock_On_Hand'] = df['Stock On Hand']
df['Cost'] = df['Average Weighted Cost'].round(2)

df['Margin'] = df.apply(lambda row: margin_calc(row['Cash_Price'], row['Cost']), axis=1).round(2)

data_to_insert = list(df[['Sku', 'Description', 'Cash_Price','Cost', 'Stock_On_Hand', 'Margin']].itertuples(index=False, name=None))

bulkInsert(data_to_insert)