from flask import Flask, make_response, redirect, url_for, request, render_template, session
import random

app = Flask(__name__)
app.secret_key = "gerald_QOO_string_key"

class UserData:

    def __init__(self, account, hashed_passwd, email, name) -> None:
        self.hashed_passwd = hashed_passwd
        self.account = account
        self.email = email
        self.name = name
        self.__pass_count:int = 0

    def set_pass_count(self):
        self.__pass_count += 1

    def get_pass_count(self):
        return self.__pass_count
    

userDatas = []

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        saved_account = request.cookies.get("registered_user", '')
        current_user = session.get("user")
        return render_template('index.html')
    else:
        input_username = request.form.get("username")
        input_passwd = request.form.get("passwd")

        target_user=None
        print(f"before check {input_username}, {input_passwd}")
        for user in userDatas:
            if user.account == input_username:
                target_user = user
                print(f"{user.account},{user.hashed_passwd},{user.email}, {user.name}")
                break
        if target_user and target_user.hashed_passwd == input_passwd:
            session["user"] = target_user.account
            return redirect(url_for("game"))
        else:
            return render_template('index.html', error_message="user name or password fail")
        
@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        passwd = request.form.get("passwd")
        email = request.form.get("email")
        name = request.form.get("name")

        userDatas.append(
            UserData(username,
                     passwd,
                     email,
                     name))
        resp = make_response(redirect(url_for("login")))
        resp.set_cookie("registered_user", username, max_age=600)
        return resp
    else: 
        return render_template('register.html')
@app.route('/game', methods = ['POST', 'GET'])
def game():
    current_user = session.get('user')
    if current_user is None:
        return redirect(url_for("login"))

    user_choice = request.args.get("choice")
    computer_choice = None
    result = None
        
    userData  = None
    print(current_user)
    print(len(userDatas))
    for user in userDatas:
        if current_user == user.account:
            userData = user

    print(f"{userData.account}, {userData.hashed_passwd}, {userData.email}, {userData.name}")

    print(user_choice)
    if user_choice:
        choices = ["paper", "scissors", "paper"]
        computer_choice = choices[ random.randint(0, 2)]
        if user_choice == computer_choice:
                result = "平手！"
        elif (user_choice == 'stone' and computer_choice == 'scissors') or \
                 (user_choice == 'scissors' and computer_choice == 'paper') or \
                 (user_choice == 'paper' and computer_choice == 'stone'):
            result = "你贏了！🎉"
            userData.set_pass_count()
        else:
            result = "你輸了...😢"

    return render_template("game.html", 
                           user=current_user, 
                           user_choice=user_choice, 
                           computer_choice=computer_choice, 
                           result=result,
                           pass_count = f"你贏了 {userData.get_pass_count()}次")

if __name__ == '__main__':
    app.run(debug = True, port=5000)
    
