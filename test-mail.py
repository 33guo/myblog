from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=25,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='240718160@qq.com',
    MAIL_PASSWORD='xzxnsskmbrmnbggd',
    MAIL_DEBUG=True
)

mail = Mail(app)

@app.route('/')
def index():
# sender 发送方哈，recipients 邮件接收方列表
    msg = Message("Hi!This is a test ",sender='240718160@qq.com', recipients=['240718160@qq.com'])
# msg.body 邮件正文 
    msg.body = "This is a first email"

    mail.send(msg)
    print( "Mail sent")


if __name__ == "__main__":
    app.run()