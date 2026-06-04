from datetime import timedelta
import os
import random
from sqliteProcess import SqliteProcess as sql
from UserDataModule import UserData as user
from werkzeug.security import generate_password_hash, check_password_hash

class LoginController:
    users: list[user] = []

    def __init__(self) -> None:
        self.sql: sql = sql()
        self.get_db_users()

    def get_db_users(self):
        rows = self.sql.get_login_data()
        if not rows:
            return

        for i in rows:
            self.users.append(user(i))

    def check_user_status(self, username:str, passwd:str):
        self.get_db_users()
        if not self.users:
            return ["index.html", "User wasn't register"]

        target_user = next((t for t in self.users if t.username == username), None)

        if target_user is None:
            return ["index.html", "User wasn't register"]

        if check_password_hash( target_user.passwd, passwd) == False:
            return ["index.html", "user name or password fail", target_user.username]
        if target_user.mail_ready == 0:
            return ["index.html", "Mail is no verify", target_user.username]

        return ["game.html", "", target_user.username]

    def user_register(self, username, passwd, email, name, front_time):
        regD = []
        dt_utc =datetime.fromtimestamp(front_time, timezone.utc) 
        regD.append(username)
        regD.append(generate_password_hash(passwd))
        regD.append(email)
        regD.append(name)
        regD.append(False)
        regD.append(random.randint(1000, 9999))
        regD.append(dt_utc)
        dt_utc_15 = dt_utc +timedelta(minutes=15)
        regD.append(dt_utc_15)
        userd = user(regD)
        userDatas.append(userd)
        # resp = make_response(redirect(url_for("login")))
        # resp.set_cookie("registered_user", username, max_age=600)
        # return resp
        # start_mail_thread(user=userd)


        

