from flask import Flask, render_template, request
from datetime import datetime as dt
from sqliteDB3 import create_table, insert, viewAll

app = Flask(__name__)
create_table()

@app.route('/', methods=['GET', 'POST'])
def home():
    year = dt.now().year
    day = dt.now().day 
    month = dt.strftime(dt.now(),'%B')
    if request.method == 'POST':
        code = request.form.get("addCode")
        model = request.form.get("addModel")
        price = request.form.get("addPrice")
        print(f"Code: {code}, Model: {model}, Price: {price}")
        insert(code, model, price)
        print("Data Inserted") 
    else:
        print("Please fill in all fields.")

    rows = viewAll()
    print(rows)
    return render_template('index.html', year=year, day=day, month=month, rows=rows) 

if __name__ == '__main__':
    app.run(debug=True)