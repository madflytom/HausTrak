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

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), unique=True)
    userId = db.Column(db.Integer)
    description = db.Column(db.String(None))

    def __init__(self, title, userId, description):
        self.title = title
        self.userId = userId
        self.description = description

    def __repr__(self):
        return '<Project %r>' % self.title

class ProjectItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), unique=True)
    projectId = db.Column(db.Integer)
    description = db.Column(db.String(None))
    cost = db.Column(db.Float)

    def __init__(self, title, projectId, description, cost):
        self.title = title
        self.projectId = projectId
        self.description = description
        self.cost = cost

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
        fields = ('id','title','projectId', 'description', 'cost')

projectItem_schema = ProjectItemSchema()
projectItems_schema = ProjectItemSchema(many=True)

class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('id','title','userId', 'description')

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

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

@app.route('/post_project', methods=['POST'])
def post_project():
    project = Project(request.form['title'], request.form['userId'], request.form['description'])
    db.session.add(project)
    db.session.commit()
    result = project_schema.dump(project)
    return jsonify(result.data)

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    result = user_schema.dump(user)
    return jsonify(result.data)

@app.route('/project')
def projects():
    projects = Project.query.all()
    result = projects_schema.dump(projects)
    return jsonify(result.data)

if __name__ == "__main__":
    app.run()