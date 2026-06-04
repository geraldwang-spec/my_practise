import os
from flask import Flask
from flask.cli import load_dotenv
from flask_mail import Mail, Message

class MailProcess:
    def __init__(self, app:Flask) -> None:
        _ = load_dotenv()
        app.secret_key = os.environ.get("SECRET_KEY")
        app.config.update(
            MAIL_SERVER='smtp.gmail.com',
            MAIL_PORT=465,
            MAIL_USE_TLS=False,
            MAIL_USE_SSL=True,
            MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
            MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
        )
        self.mail = Mail(app)
        

        



