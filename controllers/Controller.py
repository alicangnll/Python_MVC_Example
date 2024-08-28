# Controller alanı
# Tüm uygulamanın beyni buradan olacak. DB bağlantıları ve çeşitli bağlantılar dahil
# Bu alandan modele sorgular gönderilecek ve alınan cevaplar route alanında belirtilen linkte sergilenecek

from models.DBModel import User, db
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, render_template

def controller_index():
    return render_template("index.html")

def controller_insertexample():
    try:
        user = User(uname="Deneme User", upass="Parola123", umail="example@mail.com")
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 200
    except Exception as e:
        return jsonify({"message": "Error occurred (Reason : " + str(e) + ")"}), 500

def controller_userlist():
    ulist = []
    getall = User.query.all()
    for userlist in getall:
        ulist.append(userlist.uname)
    return jsonify(ulist)