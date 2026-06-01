#No need to install sqproduct3 as it is included in python3
import sqlite3

from xcelFunc import margin_calc

def insert(code, model, price, cost, stock):
    data_comm = sqlite3.connect("product.db")
    cursor = data_comm.cursor()
    cursor.execute("INSERT INTO product VALUES (?,?,?,?,?,?)", (code, model, price, cost, margin, stock))
    data_comm.commit()
    data_comm.close()
    code = ""
    model = ""
    price = ""
    cost = ""
    margin = margin_calc(cost, price)
    stock = ""

def bulkInsert(bulk_data):
    data_comm = sqlite3.connect("product.db")
    cursor = data_comm.cursor()
    cursor.executemany("INSERT OR REPLACE INTO product VALUES (?,?,?,?,?,?)", bulk_data)
    data_comm.commit()
    data_comm.close()

def viewAll():
    data_comm = sqlite3.connect("product.db")
    data_comm.row_factory = sqlite3.Row
    cursor = data_comm.cursor()
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    data_comm.close()

    formatted_rows = []
    for row in rows:
        formatted_row = dict(row)
        formatted_row['price'] = "{:.2f}".format(formatted_row['price'])
        formatted_rows.append(formatted_row)
    return formatted_rows

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
    data_comm.row_factory = sqlite3.Row
    cursor = data_comm.cursor()
    cost, margin = None, None
    if code:
        code = f"%{code}%"
        cursor.execute("SELECT * FROM product WHERE code LIKE ?", (code,))
        rows = cursor.fetchall()
        cost = rows[0]['cost']
    
    margin = margin_calc(cost, price)
    cursor.execute("UPDATE product SET model=?, price=?, margin=? WHERE code=?",
                   (model, price, margin, code))
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

    formatted_rows = []
    for row in rows:
        formatted_row = dict(row)
        formatted_row['price'] = "{:.2f}".format(formatted_row['price'])
        formatted_rows.append(formatted_row)
    return formatted_rows


