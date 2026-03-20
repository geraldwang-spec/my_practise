import csv
from itertools import product
from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def home():
    products=[]
    with open('data.csv', newline="", encoding='utf-8') as f:
        reader=csv.DictReader(f)
        for row in reader:
            products.append(row)

    return render_template('index.html', products=products)

# application = app
app.run(debug=True)
    
