from flask import Flask
from flask_cors import CORS
from flask import json
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect
from flask_marshmallow import Marshmallow
from flask import jsonify
from sqlalchemy.sql import func

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
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
    totalCost = db.Column(db.Float)
    totalTime = db.Column(db.Integer)

    def __init__(self, title, userId, description, totalCost, totalTime):
        self.title = title
        self.userId = userId
        self.description = description
        self.totalCost = totalCost
        self.totalTime = totalTime

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
        fields = ('id','title','userId', 'description', 'totalCost', 'totalTime')

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

""" User Stuff """

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

""" Project Stuff """

@app.route('/project')
def projects():
    projects = Project.query.all()
    result = projects_schema.dump(projects)
    return jsonify(result.data)

@app.route('/post_project', methods=['POST'])
def post_project():
    req_data = request.get_json()
    print(req_data)
    project = Project(req_data['title'], req_data['userId'], req_data['description'], req_data['totalCost'], req_data['totalTime'])
    
    db.session.add(project)
    db.session.commit()
    result = project_schema.dump(project)
    print(result)
    return jsonify(result.data)

@app.route('/project/<projectId>')
def project(projectId):
    project = Project.query.filter_by(id=projectId).first()

    cost = db.session.query(func.sum(ProjectItem.cost).label('totalCost')).filter(ProjectItem.projectId==projectId)
    totalCost = cost.scalar()
    print(totalCost)
    project.totalCost = totalCost

    time = db.session.query(func.sum(ProjectItem.time).label('totalTime')).filter(ProjectItem.projectId == projectId)
    totalTime = time.scalar()
    print(totalTime)
    project.totalTime = totalTime

    result = project_schema.dump(project)
    return jsonify(result.data)

""" Project Item Stuff """

@app.route('/projectItem')
def projectItems():
    projectItems = ProjectItem.query.all()
    result = projectItems_schema.dump(projectItems)
    return jsonify(result.data)

@app.route('/projectItem/<projectId>')
def getProjectItemsForProject(projectId):
    projectItems = ProjectItem.query.filter_by(projectId=projectId)
    result = projectItems_schema.dump(projectItems)
    return jsonify(result.data)

@app.route('/post_projectItem', methods=['POST'])
def post_projectItem():
    req_data = request.get_json()
    projectItem = ProjectItem(req_data['title'], req_data['projectId'], req_data['description'], req_data['cost'], req_data['time'], req_data['done'])
    db.session.add(projectItem)
    db.session.commit()
    result = projectItem_schema.dump(projectItem)
    return jsonify(result.data)

@app.route('/check_projectItem/<projectItemId>', methods=['POST'])
def check_projectItem(projectItemId):
    projectItem = ProjectItem.query.filter_by(id=projectItemId).first()
    req_data = request.get_json()
    done = req_data['done']
    projectItem.done = done
    db.session.commit()
    result = projectItem_schema.dump(projectItem)
    return jsonify(result.data)

@app.route('/delete_projectItem/<projectItemId>', methods=['DELETE'])
def delete_projectItem(projectItemId):
    projectItem = ProjectItem.query.filter_by(id=projectItemId).first()
    db.session.delete(projectItem)
    db.session.commit()
    return '', 204

if __name__ == "__main__":
    app.run()