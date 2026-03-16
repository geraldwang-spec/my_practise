from typing import LiteralString
from flask import Flask, Response, jsonify, request, send_file,render_template

app:Flask = Flask(import_name=__name__)

@app.route("/")
def home()->str:
    return "Flask API OK Test one more time"

@app.route("/news")
def news()->Response:
    data:list[dict[str,str]]=[
            {'title':'first news','url':'http://example.com/1'},
            {'title':'first news','url':'http://example.com/2'},
            {'title':'first news','url':'http://example.com/3'}
            ]
    return jsonify(data)

@app.route('/calc')
def calc():
    a=request.args.get('a', 0)
    b=request.args.get('b', 0)
    a = int(a)
    b=int(b)
    return str(a+b)

@app.route('/images')
def get_picture()->LiteralString:
    return '''
        <h2>show picture</h2>
        <img src="/static/dog1.jpg" width="300">
        <img src="/static/dog2.png" width="300">
    '''

@app.route('/images2')
def get_picture_onlin()->LiteralString:
    return '''
        <h1>animail picture</h1>
        <a href="/photo?name=dog">dog</a><br>
        <a href="/photo?name=cat">cat</a><br>
        <a href="/dogs">dogs</a><br>
    '''

@app.route('/photo')
def photo()->Response:
    name=request.args.get("name", "dog")
    path=f"static/{name}.jpg"
    return send_file((path))

@app.route('/dogs')
def dogs()->str:
    html:str ="<h1>dogs picture</h1>"
    for i in range(1,6):
        html+= f'<img src="/static/dog{i}.jpg" width="200">'
    return html

# @app.route('/render_template_ex')
# def render_template_ex()->str:
#     return render_template(template_name_or_list="index.html")

if __name__ == "__main__":
    app.run(debug=True)
