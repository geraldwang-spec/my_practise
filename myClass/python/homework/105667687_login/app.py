from flask import Flask, make_response, redirect, url_for, request, render_template, session
from flask_mail import Mail, Message
from threading import Thread
from login_controller import LoginController as loginC


def create_app(loginParam:loginC)->Flask:
    app = Flask(__name__)
    # app.secret_key = "gerald_QOO_string_key"
    #
    # app.config.update(
    #     MAIL_SERVER='smtp.gmail.com',
    #     MAIL_PORT=465,
    #     MAIL_USE_TLS=False,
    #     MAIL_USE_SSL=True,
    #     MAIL_USERNAME="g123erald456@gmail.com",
    #     MAIL_PASSWORD="bjnasfhhodnvigwl"
    # )
    # mail = Mail(app)

    @app.route("/", methods=['POST', "GET"])
    def login():
        if request.method == "GET":
            return render_template('index.html')
        else:
            dic = loginParam.check_user_status(request.form.get("username"), request.form.get("passwd"))
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
        
            userd = UserData(username,
                         passwd,
                         email,
                         name)
            userDatas.append(userd)
            # resp = make_response(redirect(url_for("login")))
            # resp.set_cookie("registered_user", username, max_age=600)
            # return resp
            start_mail_thread(user=userd)
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

def init_app():
    login = loginC()

    return login
    

if __name__ == '__main__':
    flask_app = create_app(init_app())
    flask_app.run(debug = True, port=5000)
    
