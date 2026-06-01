from queue import Empty
from flask import Flask, make_response, redirect, url_for, request, render_template, session
from flask_mail import Mail, Message
import random
from threading import Thread


app = Flask(__name__)
app.secret_key = "gerald_QOO_string_key"

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME="g123erald456@gmail.com",
    MAIL_PASSWORD="bjnasfhhodnvigwl"
)
mail = Mail(app)

class UserData:

    def __init__(self, account:str, hashed_passwd:str, email:str, name:str) -> None:
        self.hashed_passwd = hashed_passwd
        self.account = account
        self.email = email
        self.name = name
        self.__pass_count:int = 0
        self.__mail_check:bool = False
        self.__mail_check_number:int = 0

    def set_pass_count(self):
        self.__pass_count += 1

    def get_pass_count(self):
        return self.__pass_count

    def set_mail_check(self):
        self.__mail_check = True

    def get_mail_check(self):
        return self.__mail_check

    def get_mail_check_number(self)->int:
        if self.__mail_check_number == 0:
            self.__mail_check_number = random.randint(1, 9999)
        return self.__mail_check_number
    

userDatas = []

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        saved_account = request.cookies.get("registered_user", '')
        current_user = session.get("user", "")
        if len(current_user) != 0:
            return render_template("game.html", user = current_user)
        return render_template('index.html', user = current_user)
    else:
        input_username = request.form.get("username")
        input_passwd = request.form.get("passwd")

        target_user = next((t for t in userDatas if t.account == input_username), None)
        # target_user=None
        # for user in userDatas:
        #     if user.account == input_username:
        #         target_user = user
        #         print(f"{user.account},{user.hashed_passwd},{user.email}, {user.name}")
        #         break

        if target_user is None:
            return render_template('index.html', error_message="user name or password fail")

        if target_user.hashed_passwd != input_passwd:
            return render_template('index.html', 
                                   error_message="user name or password fail",
                                  user = target_user.account )
        
        if target_user.get_mail_check() != True:
            return render_template('index.html', 
                                   error_message="Mail is not verify",
                                  user = target_user.account )

        resp = make_response(redirect(url_for("game")))
        resp.set_cookie("registered_user", input_username, max_age=600)
        session["user"] = input_username
        return resp
        # return redirect(url_for("game"))
        
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

def start_mail_thread(user:UserData):
    msg_title = 'Hello It is checking mail'
    #  寄件者，若參數有設置就不需再另外設置
    msg_sender = 'Sender Mail@mail_domain.com'
    #  收件者，格式為list，否則報錯
    print(f"{user.email}")
    msg_recipients = [user.email]
    #  郵件內容
    # msg_body = 'Hey, I am mail body!'
    # 也可以利用html做內容
    msg_html = f'<h1>Hey, this is verify mail. Please click <a href=\"http://127.0.0.1:5000/mailcheck?user={user.name}&mail_number={user.get_mail_check_number()}\">this</a></h1>'
    msg = Message(msg_title,
                  sender=msg_sender,
                  recipients=msg_recipients)
    # msg.body = msg_body
    msg.html = msg_html

    #  使用多線程
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return 'You Send Mail by Flask-Mail Success!!'


def send_async_email(app, msg):
    #  下面有說明
    with app.app_context():
        mail.send(msg)

@app.route('/game', methods = ['POST', 'GET'])
def game():
    current_user = session.get('user')
    if current_user is None:
        return redirect(url_for("login"))

    user_choice = request.args.get("choice")
    computer_choice = None
    result = ""
        
    userData  = None
    for user in userDatas:
        if current_user == user.account:
            userData = user

    print(f"{userData.account}, {userData.hashed_passwd}, {userData.email}, {userData.name}")

    print(user_choice)
    if user_choice:
        choices = ["paper", "scissors", "tone"]
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

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/mailcheck")
def mailcheck():
    user_name = request.args.get("user", "")
    user_mail_number = request.args.get("mail_number", "")

    if user_name == "" or user_mail_number == "":
        return render_template("mailcheck.html", message = "Parameter Fail, Please re-register again")

    userd = next((t for t in userDatas if t.name == user_name ), None)

    if userd is None:
        print("None")
        return render_template("mailcheck.html", message = "Register Fail, Please re-register again")
    
    if int(user_mail_number) != userd.get_mail_check_number():
        return render_template("mailcheck.html", message = "Register Fail, Please re-register again")

    userd.set_mail_check()
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug = True, port=5000)
    
