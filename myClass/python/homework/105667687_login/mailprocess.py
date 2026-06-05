from flask import Flask
from flask_mail import Mail, Message
from threading import Thread

class MailProcess:
    mail: Mail
    app: Flask
    def __init__(self, app:Flask) -> None:
        self.mail = Mail(app)
        self.app = app
        
    def start_mail_thread(self, user:UserData):
        msg_title = 'Hello It is checking mail'
        #  寄件者，若參數有設置就不需再另外設置
        msg_sender = 'Sender Mail@mail_domain.com'
        #  收件者，格式為list，否則報錯
        print(f"{user.email}")
        msg_recipients = [user.email]
        #  郵件內容
        # msg_body = 'Hey, I am mail body!'
        # 也可以利用html做內容
        msg_html:str = f'<h1>Hey, this is verify mail. Please click <a href=\"http://127.0.0.1:5000/mailcheck?user={user.name}&mail_number={user.get_mail_check_number()}\">this</a></h1>'
        msg = Message(msg_title,
                      sender=msg_sender,
                      recipients=msg_recipients)
        # msg.body = msg_body
        msg.html = msg_html
    
        #  使用多線程
        thr = Thread(target=send_async_email, args=[app, msg])
        thr.start()
        return 'You Send Mail by Flask-Mail Success!!'
    
    
    def send_async_email(self, app, msg):
    #  下面有說明
         with self.app.app_context():
            self.mail.send(msg)


        



