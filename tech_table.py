import sqlite3
from xml.parsers.expat import model

def create_tech_table():
    data_comm = sqlite3.connect("tech.db")
    cursor = data_comm.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tech (" \
        "model TEXT PRIMARY KEY, " \
        "tech_1 TEXT, " \
        "tech_2 TEXT, " \
        "resolution TEXT)"
    )
    data_comm.commit()
    data_comm.close()

def insert_tech(model, tech_1, tech_2, resolution):
    data_comm = sqlite3.connect("tech.db")
    cursor = data_comm.cursor()
    cursor.execute("INSERT INTO tech VALUES (?,?,?,?)", (model, tech_1, tech_2, resolution))
    data_comm.commit()
    data_comm.close()
    model = ""
    tech_1 = ""
    tech_2 = ""
    resolution = ""

def bulkInsert_tech(bulk_data):
    data_comm = sqlite3.connect("tech.db")
    cursor = data_comm.cursor()
    cursor.executemany("INSERT OR IGNORE INTO tech VALUES (?,?,?,?,?,?)", bulk_data)
    data_comm.commit()
    data_comm.close()

def viewAll_tech():
    data_comm = sqlite3.connect("tech.db")
    data_comm.row_factory = sqlite3.Row
    cursor = data_comm.cursor()
    cursor.execute("SELECT * FROM tech")
    rows = cursor.fetchall()
    data_comm.close()

    formatted_rows = []
    for row in rows:
        formatted_row = dict(row)
        formatted_rows.append(formatted_row)
    return formatted_rows

def delete(model, tech_1, tech_2, resolution):
    data_comm = sqlite3.connect("tech.db")
    cursor = data_comm.cursor()
    cursor.execute("DELETE FROM tech WHERE model=? OR tech_1=? OR tech_2=? OR resolution=?", (model, tech_1, tech_2, resolution))
    data_comm.commit()
    data_comm.close()

def deleteAll_tech():
    data_comm = sqlite3.connect("tech.db")
    cursor = data_comm.cursor()
    cursor.execute("DELETE FROM tech")
    data_comm.commit()
    data_comm.close()
    print("Everything Deleted")

def update_tech(model, tech_1, tech_2, resolution):
    data_comm = sqlite3.connect("tech.db")
    cursor = data_comm.cursor()
    cursor.execute("UPDATE tech SET model=?, tech_1=?, tech_2=?, resolution=? WHERE model=?",
                   (model, tech_1, tech_2, resolution, model))
    data_comm.commit()
    data_comm.close()

def searchDB_tech(search_term):
    data_comm = sqlite3.connect("tech.db")
    data_comm.row_factory = sqlite3.Row
    cursor = data_comm.cursor()
    if search_term:
        search_term = f"%{search_term}%"
        cursor.execute("SELECT * FROM tech WHERE model LIKE ? OR tech_1 LIKE ? OR tech_2 LIKE ? OR resolution LIKE ?", (search_term, search_term, search_term, search_term))
    rows = cursor.fetchall()
    data_comm.close()

    formatted_rows = []
    for row in rows:
        formatted_row = dict(row)
        formatted_rows.append(formatted_row)
    return formatted_rows
