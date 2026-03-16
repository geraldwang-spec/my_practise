from flask import Flask, render_template

app:Flask = Flask(import_name=__name__)

@app.route("/")
def home()->str:
    return render_template(template_name_or_list="index.html")

@app.route('/dog')
def dog():
    return "<h1>dog picture</h1>"

@app.route('/cat')
def cat():
    return "<h1>cat picture</h1>"

if __name__ == "__main__":
    app.run(debug=True)
