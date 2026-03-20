from flask import Flask, render_template
from flask_cors import CORS

def create_app()->Flask:
    app:Flask = Flask(import_name=__name__)

    CORS(app)

    @app.route('/')
    def home()->str:
        return render_template(template_name_or_list='index.html')

    @app.route('/test01')
    def test01()->dict[str,str]:
        return {"apple":"QOO"}

    return app

if __name__ == "__main__":
    stock_app:Flask = create_app()
    stock_app.run(debug=True, port=8000)
    
 
