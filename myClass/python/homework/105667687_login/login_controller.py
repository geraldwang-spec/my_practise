from asyncio.windows_events import NULL
from datetime import datetime, timezone, timedelta
import os
import random
from flask import Flask
from flask.cli import load_dotenv
from sqlalchemy import null
from werkzeug.security import generate_password_hash, check_password_hash
from sqliteProcess import DatabaseManager
from UserDataModule import UserData as user
from mailprocess import MailProcess as mailp

class LoginController:
    users: list[user] = []
    app: Flask
    __mailproc: mailp
    __db_m:DatabaseManager

    def __init__(self, _app:Flask) -> None:
        self.app = _app
        # self.sql: sql = sql()
        # self.get_db_users()

    def init_core(self)->None:
        _ = load_dotenv()
        self.app.secret_key = os.environ.get("SECRET_KEY")
        self.app.config.update(
            MAIL_SERVER='smtp.gmail.com',
            MAIL_PORT=465,
            MAIL_USE_TLS=False,
            MAIL_USE_SSL=True,
            MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
            MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
        )
        self.__mailproc = mailp(self.app)
        self.__db_m = DatabaseManager()

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
        print(front_time)
        regD = []
        dt_utc =datetime.fromtimestamp(float(front_time), timezone.utc) 
        regD.append(username)
        regD.append(generate_password_hash(passwd))
        regD.append(email)
        regD.append(name)
        regD.append(False)
        regD.append(random.randint(1000, 9999))
        regD.append(dt_utc)
        dt_utc_15 = dt_utc +timedelta(minutes=15)
        regD.append(dt_utc_15)
        # self.users.append(user(regD))
        print(dt_utc) 
        

