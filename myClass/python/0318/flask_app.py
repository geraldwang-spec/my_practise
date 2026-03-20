from flask import Flask,render_template
import csv

app = Flask(__name__)

@app.route('/')
def home():
    titles_data=[]

    csv_path='/home/geraldQOO/mysite/ptt_nba.csv'

    with open(csv_path,newline='',encoding='utf-8-sig') as f:
        reader=csv.DictReader(f)

        for row in reader:
            titles_data.append({
                    'title':row['title'],
                    'link':row['link'],
                })



    return render_template("index.html",titles=titles_data)

#PYanywhere 需要這一行
application=app

