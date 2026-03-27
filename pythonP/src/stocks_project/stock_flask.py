from flask import Flask, Response, jsonify, render_template
from flask_cors import CORS
from stocks_project.stock_process import stock_process_module

def create_app()->Flask:
    app:Flask = Flask(import_name=__name__)

    CORS(app)

    @app.route('/')
    def home()->str:
        return render_template(template_name_or_list='index.html')

    @app.route('/test01')
    def test01()->dict[str,str]:
        return {"apple":"QOO"}

    @app.route('/stocks_price')
    def stocks_price()->Response:
        stock_p:stock_process_module = stock_process_module()
        sample_data:list[dict[str,str]] = stock_p.process_stocks_data(select=0)

        return jsonify(sample_data)

    @app.route(rule='/login')
    def login_page()->str:
        return render_template(template_name_or_list='login.html')

    @app.route(rule='/games')
    def games()->str:
        return render_template(template_name_or_list='games.html')

    @app.route(rule='/camera')
    def camera_test()->str:
        return render_template(template_name_or_list='camera.html')

    return app

if __name__ == "__main__":
    stock_app:Flask = create_app()
    stock_app.run(debug=True, port=8000)
    
 
