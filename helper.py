
from tabulate import tabulate
from db_tables import product

from db_tables.tables import create_prod_table

#create_prod_table()


prods = product.viewAll()

print(tabulate(prods, headers="keys", tablefmt="grid"))




