import os
from flask import Flask, make_response, redirect, url_for, request, render_template, session
from flask.cli import load_dotenv
# from flask_mail import Mail, Message
# from threading import Thread
from login_controller import LoginController as loginC
from mailprocess import MailProcess


def create_app()->Flask:
    app = Flask(__name__)
    # mail = Mail(app)
    #
    loginCore = loginC(app)
    loginCore.init_core()
    

    @app.route("/", methods=['POST', "GET"])
    def login():
        if request.method == "GET":
            return render_template('index.html')
        else:
            dic = loginCore.check_user_status(request.form.get("username"), request.form.get("passwd"))
            if len(dic) == 2:
                return render_template(dic[0], error_message=dic[1])
            elif len(dic) == 3:
                return render_template(dic[0], error_message=dic[1], user=dic[2])

    @app.route('/register', methods = ['POST','GET'])
    def register():
        if request.method == 'POST':
            username = request.form.get("username")
            passwd = request.form.get("passwd")
            email = request.form.get("email")
            name = request.form.get("name")
            localTime = request.form.get("client_timestamp")
            print(f"local = {localTime}")

            loginCore.user_register(username, passwd, email, name, localTime)
            return render_template("index.html")
        else: 
            return render_template('register.html')
    
    @app.route('/game', methods = ['POST', 'GET'])
    def game():
    
        return render_template("game.html" )   
    @app.route("/logout")
    def logout():
        return redirect(url_for("login"))
    
    @app.route("/mailcheck")
    def mailcheck():
        return redirect(url_for("login"))

    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug = True, port=5000)
    
