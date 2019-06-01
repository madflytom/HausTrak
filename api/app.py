from flask import Flask
from flask_cors import CORS
from flask import json
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect
from flask_marshmallow import Marshmallow
from flask import jsonify
from sqlalchemy.sql import func
from flask.ext.heroku import Heroku

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/haustrak'
heroku = Heroku(app)
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

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), unique=True)
    userId = db.Column(db.Integer)
    description = db.Column(db.String(None))
    totalCost = db.Column(db.Float)
    totalTime = db.Column(db.Integer)
    auth0subject = db.Column(db.String(250))

    def __init__(self, title, userId, description, totalCost, totalTime, auth0subject):
        self.title = title
        self.userId = userId
        self.description = description
        self.totalCost = totalCost
        self.totalTime = totalTime
        self.auth0subject = auth0subject

    def __repr__(self):
        return '<Project %r>' % self.title

class ProjectItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), unique=True)
    projectId = db.Column(db.Integer)
    description = db.Column(db.String(None))
    cost = db.Column(db.Float)
    time = db.Column(db.Integer)
    done = db.Column(db.Boolean)

    def __init__(self, title, projectId, description, cost, time, done):
        self.title = title
        self.projectId = projectId
        self.description = description
        self.cost = cost
        self.time = time
        self.done = done

    def __repr__(self):
        return '<ProjectItem %r>' % self.title

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','username','email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class ProjectItemSchema(ma.Schema):
    class Meta:
        fields = ('id','title','projectId', 'description', 'cost', 'time', 'done')

projectItem_schema = ProjectItemSchema()
projectItems_schema = ProjectItemSchema(many=True)

class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('id','title','userId', 'description', 'totalCost', 'totalTime', 'auth0subject')

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

from routes import *
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run()