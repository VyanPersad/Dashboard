import sqlite3

def create_model_table():
    data_comm = sqlite3.connect("model_brand.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS model (" \
        "code TEXT PRIMARY KEY, " \
        "model TEXT, " \
        "brand TEXT, " \
        "sku_class TEXT)"
    )
    data_comm.commit()
    data_comm.close()

def insert_mb(code, model, brand, sku_class):
    data_comm = sqlite3.connect("model_brand.db")
    cursor = data_comm.cursor()
    cursor.execute("INSERT INTO model VALUES (?,?,?,?)", (code, model, brand, sku_class))
    data_comm.commit()
    data_comm.close()
    code = ""
    model = ""
    brand = ""
    sku_class = ""

def bulkInsert_mb(bulk_data):
    data_comm = sqlite3.connect("model_brand.db")
    cursor = data_comm.cursor()
    cursor.executemany("INSERT OR IGNORE INTO model VALUES (?,?,?,?)", bulk_data)
    data_comm.commit()
    data_comm.close()

def viewAll_mb():
    data_comm = sqlite3.connect("model_brand.db")
    data_comm.row_factory = sqlite3.Row
    cursor = data_comm.cursor()
    cursor.execute("SELECT * FROM model")
    rows = cursor.fetchall()
    data_comm.close()

    formatted_rows = []
    for row in rows:
        formatted_row = dict(row)
        formatted_row['price'] = "{:.2f}".format(formatted_row['price'])
        formatted_rows.append(formatted_row)
    return formatted_rows

def delete_mb(code):
    data_comm = sqlite3.connect("model_brand.db")
    cursor = data_comm.cursor()
    cursor.execute("DELETE FROM model WHERE code=?", (code, ))
    data_comm.commit()
    data_comm.close()

def deleteAll_mb():
    data_comm = sqlite3.connect("model_brand.db")
    cursor = data_comm.cursor()
    cursor.execute("DELETE FROM model")
    data_comm.commit()
    data_comm.close()
    print("Everything Deleted")

def update_mb(code, model, brand, sku_class):
    data_comm = sqlite3.connect("model_brand.db")
    cursor = data_comm.cursor()
    cursor.execute("UPDATE model SET model=?, brand=?, sku_class=? WHERE code=?",
                   (model, brand, sku_class, code))
    data_comm.commit()
    data_comm.close()

def searchDB_mb(search_term):
    data_comm = sqlite3.connect("model_brand.db")
    data_comm.row_factory = sqlite3.Row
    cursor = data_comm.cursor()
    if search_term:
        search_term = f"%{search_term}%"
        cursor.execute("SELECT * FROM model WHERE code LIKE ? OR model LIKE ? OR brand LIKE ? OR sku_class LIKE ?", (search_term, search_term, search_term, search_term))
    rows = cursor.fetchall()
    data_comm.close()

    formatted_rows = []
    for row in rows:
        formatted_row = dict(row)
        formatted_row['price'] = "{:.2f}".format(formatted_row['price'])
        formatted_rows.append(formatted_row)
    return formatted_rows
