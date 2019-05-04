from flask import Flask
from flask import json
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect
from flask_marshmallow import Marshmallow
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/haustrak'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','username','email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/')
def index():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result.data)

@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    username = request.form['username']
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(username=username).first()
    result = user_schema.dump(user)
    return jsonify(result.data)

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    result = user_schema.dump(user)
    return jsonify(result.data)

if __name__ == "__main__":
    app.run()