#No need to install sqproduct3 as it is included in python3
import sqlite3

def create_table():
    data_comm = sqlite3.connect("product.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS product (code TEXT, model TEXT, price REAL)"
    )
    data_comm.commit()
    data_comm.close()


def insert(code, model, price):
    data_comm = sqlite3.connect("product.db")
    cursor = data_comm.cursor()
    cursor.execute("INSERT INTO product VALUES (?,?,?)", (code, model, price))
    data_comm.commit()
    data_comm.close()

def viewAll():
    data_comm = sqlite3.connect("product.db")
    data_comm.row_factory = sqlite3.Row
    cursor = data_comm.cursor()
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    data_comm.close()
    return rows

def delete(code):
    data_comm = sqlite3.connect("product.db")
    cursor = data_comm.cursor()
    cursor.execute("DELETE FROM product WHERE code=?", (code, ))
    data_comm.commit()
    data_comm.close()

def deleteAll():
    data_comm = sqlite3.connect("product.db")
    cursor = data_comm.cursor()
    cursor.execute("DELETE FROM product")
    data_comm.commit()
    data_comm.close()
    print("Everything Deleted")

def update(code, model, price):
    data_comm = sqlite3.connect("product.db")
    cursor = data_comm.cursor()
    cursor.execute("UPDATE product SET model=?, price=? WHERE code=?",
                   (model, price, code))
    data_comm.commit()
    data_comm.close()

def searchDB(search_term):
    data_comm = sqlite3.connect("product.db")
    data_comm.row_factory = sqlite3.Row
    cursor = data_comm.cursor()
    if search_term:
        search_term = f"%{search_term}%"
        cursor.execute("SELECT * FROM product WHERE code LIKE ? OR model LIKE ? OR price LIKE ?", (search_term, search_term, search_term))
    rows = cursor.fetchall()
    data_comm.close()
    return rows

'''
#create_table()

insert("Wine Glass", 12, 12.50)
insert("Beer Glass", 6, 10.50)
insert("Tea Cup", 6, 3.50)

print(viewAll())
delete("Wine Glass")
delete("Beer Glass")
update(5, 4.50, "Tea Cup")
print(viewAll())
deleteAll()
print(viewAll())
'''
