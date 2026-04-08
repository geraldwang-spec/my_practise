import os
from tempfile import template
from flask import Flask, Response, jsonify, render_template, request
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

    @app.route(rule='/cie1931')
    def cie1931()->str:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(current_dir, 'templates', 'cie1931_chromaticity.html')
        a:int = int(request.args.get('a', 0))
        print(f"test a = {a}")

        print(f"--- try read file: {template_path} ---")

        if not os.path.exists(template_path):
            return f"can't find file, please check path: {template_path}"

        mtime=os.path.getmtime(template_path)
        return render_template(template_name_or_list='cie1931_chromaticity.html', mtime=mtime)

    @app.route(rule='/cie1931_2')
    def cie1931_2()->str:
        return render_template(template_name_or_list='cie1931_chat.html')

    @app.route('/camera2')
    def camera2()->str:
        return render_template(template_name_or_list='camera2.html')

    return app

if __name__ == "__main__":
    stock_app:Flask = create_app()
    stock_app.config['TEMPLATES_AUTO_RELOAD'] = True
    stock_app.run(debug=True, port=8000)
    
 
