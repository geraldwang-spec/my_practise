from flask import Flask, request

def create_app()->Flask:
    app:Flask = Flask(import_name=__name__)

    @app.route('/')
    def home()->str:
        return "apple"

    @app.route('/add')
    def add()->str:
        a:int = int(request.args.get('a', 0))
        b:int = int(request.args.get('b', 0))
        return str(a+b)

    return app

if __name__ == "__main__":
    my_app:Flask = create_app()
    my_app.run(debug=True, port=8000)

