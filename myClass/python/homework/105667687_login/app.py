from unittest import result
from flask import Flask, Response, make_response, redirect, url_for, request, render_template, session
from login_controller import AuthStatus, LoginController as loginC, LoginResponse
from sqliteProcess import GameModule


def create_app()->Flask:
    app = Flask(__name__)
    loginCore = loginC(app)
    loginCore.init_core()

    @app.route("/", methods=['POST', "GET"])
    def login():
        if request.method == "GET":
            current_user = session.get("user", "")
            if current_user:
                return render_template("game.html", user = current_user)
            return render_template('index.html', user = current_user)
        else:
            user_name =request.form.get("username", "")
            pass_wd =request.form.get("passwd","") 
            res:LoginResponse = loginCore.check_user_status(
                username=user_name,
                passwd=pass_wd)
        
        if res.status == AuthStatus.USER_NOT_FOUND or \
            res.status == AuthStatus.MAIL_NOT_VERIFIED:
            return render_template(
                    template_name_or_list="index.html",
                    error_message = res.error_message)
        
        if res.status == AuthStatus.PASSWORD_ERROR:
            res_user:GameModule|None = res.extra_data
            if res_user is None:
                return render_template(
                template_name_or_list="index.html",
                error_message="extra_data failed"
            )
            return render_template(
                template_name_or_list= "index.html", 
                    error_message = res.error_message,
                    user = res_user.user_name)
        
        resp:Response = make_response(redirect(location=url_for(endpoint="game")))
        resp.set_cookie(key="registered_user", value=user_name, max_age=600)
        session["user"] = user_name
        return resp

    @app.route('/register', methods = ['POST','GET'])
    def register():
        if request.method == 'POST':
            user_name:str = request.form.get("username", "")
            passwd:str = request.form.get("passwd", "")
            email:str = request.form.get("email", "")
            name:str = request.form.get("name", "")

            get_data:LoginResponse= loginCore.user_register(user_name, passwd, email, name)

            if get_data.status != AuthStatus.SUCCESS:
                return render_template(
                    template_name_or_list="register",
                    error_message = get_data.error_message)

            return redirect(location=url_for(endpoint="login"))
        else: 
            return render_template('register.html')
    
    @app.route('/game', methods = ['POST', 'GET'])
    def game():
        current_user = session.get('user', "") 
        if current_user is None:
            return redirect(url_for("login"))

        user_choice:str | None = request.args.get("choice")
        if user_choice is None:
            return render_template(
                "game.html",
                user = current_user,
                pass_count = f"{current_user} is not choice")
 
        res:LoginResponse = loginCore.game_process(input_user_name=current_user,input_user_choice=user_choice)

        game_user:GameModule|None = res.extra_data
        if game_user is None:
            return render_template(
                template_name_or_list="game.html",
                user=current_user,
                pass_count="extra_data failed"
            )
        
        if res.status != AuthStatus.SUCCESS:
            return render_template(
                template_name_or_list="game.html",
                user = game_user.user_name,
                result = res.error_message)

        return render_template(
            template_name_or_list="game.html",
            user = game_user.user_name,
            user_choice = game_user.user_choice,
            computer_choice = game_user.computer_choice,
            pass_count = game_user.pass_count,
            result = game_user.result
        )

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login"))
    
    @app.route("/mailcheck")
    def mailcheck():
        res:LoginResponse = loginCore.get_check_mail(
            user_name=request.args.get("user",""), 
            number=request.args.get("mail_number",""))

        if res.status != AuthStatus.SUCCESS:
            return render_template(
                template_name_or_list="mailcheck.html",
                message = res.error_message)

        return redirect(location=url_for(endpoint="login"))

    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug = True, port=5000)
    
