from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home()->str:
    return render_template("index.html")

# #PYanywhere has to below command
# application=app
if __name__ == "__main__":
    app.run(debug=True)


