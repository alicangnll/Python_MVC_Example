# Database'i oluşturan alan
# Dilerseniz farklı tabloları aynı mantıkla alt satırlara ekleyebilirsiniz.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'userlist'
    userid = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(120))
    upass = db.Column(db.String(120))
    umail = db.Column(db.String(120))
    @property
    def serialize(self):
        return {
            'user_id': self.userid,
            'user_name': self.uname,
            'user_pwd': self.upass,
            'user_mail': self.umail
        }