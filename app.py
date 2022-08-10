# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask, render_template
# from datetime import datetime
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
#
# db = SQLAlchemy(app)
#
# class Users(db.Model):
#
#     id = db.Column(db.Integer, primaty_key=True)
#     email = db.Column(db.String(50, unique=True))
#     psw = db.Column(db.String(500), nullable=True)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f"<users {self.id}"
#
# class Profiles(db.Model):
#     id = db.Column(db.Integer, primaty_key=True)
#     name = db.Column(db.String(50, nullable=True))
#     old = db.Column(db.Integer)
#     city = db.Column(db.String(100))
#
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     def __repr__(self):
#         return f"profiles {self.id}"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)



