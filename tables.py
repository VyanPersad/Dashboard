import sqlite3

def create_model_table():
    data_comm = sqlite3.connect("model.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS model (" \
        "code TEXT PRIMARY KEY, " \
        "model TEXT, " \
        "class TEXT)"
    )
    data_comm.commit()
    data_comm.close()

def create_brand_table():
    data_comm = sqlite3.connect("brand.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS brand (" \
        "code TEXT PRIMARY KEY, " \
        "brand TEXT, " \
        "model TEXT, " \
        "description TEXT)"
    )
    data_comm.commit()
    data_comm.close()

def create_tech_table():
    data_comm = sqlite3.connect("tech.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tech (" \
        "model TEXT PRIMARY KEY, " \
        "tech TEXT, " \
        "resolution TEXT)"
    )
    data_comm.commit()
    data_comm.close()

def create_costing_table():
    data_comm = sqlite3.connect("costing.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS costing (" \
        "code TEXT PRIMARY KEY, " \
        "cost REAL, " \
        "margin REAL)"
    )
    data_comm.commit()
    data_comm.close()

def create_discount_table():
    data_comm = sqlite3.connect("discount.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS discount (" \
        "code TEXT PRIMARY KEY, " \
        "discount_cash REAL), " "discount_percent REAL), " \
        "discounted_price REAL)"                
    )
    data_comm.commit()
    data_comm.close()