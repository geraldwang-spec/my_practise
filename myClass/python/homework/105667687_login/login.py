from flask import Flask, redirect, url_for, request, render_template

class UserData:
    def __init__(self, account, passwd, email, name) -> None:
        self.account = account
        self.passwd = passwd
        self.email = email
        self.name = name

app = Flask(__name__)

userDatas = []

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == "GET":
        account = request.args.get("account", "")
        return render_template('login.html', account=account)
    else:
        account = request.form.get("account")
        passwd = request.form.get("passwd")
        if len(userDatas) == 0:
            return redirect(url_for('register'))
        return render_template('login.html', account=account)
        
@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        userDatas.append(
            UserData(request.form.get("account"),
                     request.form.get("passwd"),
                     request.form.get("email"),
                     request.form.get("name")))
        return redirect(url_for("login", account = request.form.get("account")))
    else: 
        return render_template('register.html')
    

if __name__ == '__main__':
    app.run(debug = True)
    
