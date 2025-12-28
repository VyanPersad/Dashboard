from xcelFunc import read_from_file
from sqliteDB3 import insert, bulkInsert


df = read_from_file('resources\\BuyerSalesHistory.csv', test=0, n=0, col_Names = ['Sku','Brand', 'Description', 'Cash Price','Year'], searchTerm='This Year', searchCol='Year')
df['Cash_Price'] = df['Cash Price']

data_to_insert = list(df[['Sku', 'Description', 'Cash_Price']].itertuples(index=False, name=None))

bulkInsert(data_to_insert)