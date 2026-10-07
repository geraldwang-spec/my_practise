from ast import main
from flask import Blueprint, Flask, render_template, request
from ML.ml_route import create_mlapi
from llmapi.llmapi_route import create_llmapi


def create_app()->Flask:
    app = Flask(import_name=__name__)

    llmapi_blueprint:Blueprint= create_llmapi()
    app.register_blueprint(blueprint=llmapi_blueprint)
    mlapi_blueprint:Blueprint = create_mlapi()
    app.register_blueprint(blueprint=mlapi_blueprint)

    @app.route("/")
    def home():
        return render_template(template_name_or_list="index.html")


    return app


if __name__ == "__main__":
    flask_app = create_app()
    # flask_app.run(host="0.0.0.0", debug=True, port=5000)
    flask_app.run(host="0.0.0.0", debug=True, port=5000)
