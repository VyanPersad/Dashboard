import sqlite3

def create_prod_table():
    data_comm = sqlite3.connect("product.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS product (" \
        "code TEXT PRIMARY KEY, " \
        "model TEXT, " \
        "price REAL, " \
        "cost REAL, " \
        "margin REAL, " \
        "stock INTEGER)"
    )
    data_comm.commit()
    data_comm.close()

def create_model_table():
    data_comm = sqlite3.connect("model_brand.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS model (" \
        "code TEXT PRIMARY KEY, " \
        "model TEXT, " \
        "brand TEXT, " \
        "class TEXT)"
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

def create_promo_table():
    data_comm = sqlite3.connect("promo.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS promo (" \
        "code TEXT PRIMARY KEY, " \
        "discount_cash REAL, " \
        "discount_percent REAL, " \
        "discounted_price REAL," \
        "date_start DATE," \
        "date_end DATE)"              
    )
    data_comm.commit()
    data_comm.close()

def create_stk_table():
    data_comm = sqlite3.connect("stock.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS stock (" \
        "code TEXT PRIMARY KEY, " \
        "date DATE, " \
        "stk_in_stores REAL, " \
        "stk_in_wh REAL, " \
        "stk_in_serviTech REAL)"                
    )
    data_comm.commit()
    data_comm.close()

def create_features_table():
    data_comm = sqlite3.connect("features.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS features (" \
        "model TEXT PRIMARY KEY, " \
        "f_1 TEXT, " \
        "f_2 TEXT, " \
        "f_3 TEXT, " \
        "f_4 TEXT, " \
        "f_5 TEXT)"
    )
    data_comm.commit()
    data_comm.close()