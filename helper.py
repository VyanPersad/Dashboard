from db_tables import product

from db_tables.tables import create_prod_table

#create_prod_table()


prods = product.viewAll()

for prod in prods:
    print(prod)




