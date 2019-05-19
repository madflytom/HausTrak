from flask import Blueprint

from . import routes

from app import db
from app import Project
from app import projects_schema
from app import project_schema
from app import ProjectItem

from flask import jsonify
from sqlalchemy.sql import func
from flask import render_template, url_for, request, redirect

@routes.route('/project')
def projects():
    projects = Project.query.all()
    fullProjects = []

    for project in projects:
        cost = db.session.query(func.sum(ProjectItem.cost).label('totalCost')).filter(ProjectItem.projectId==project.id)
        totalCost = cost.scalar()
        print(totalCost)
        project.totalCost = totalCost

        time = db.session.query(func.sum(ProjectItem.time).label('totalTime')).filter(ProjectItem.projectId == project.id)
        totalTime = time.scalar()
        print(totalTime)
        project.totalTime = totalTime
        fullProjects.append(project)

    result = projects_schema.dump(fullProjects)
    return jsonify(result.data)

@routes.route('/post_project', methods=['POST'])
def post_project():
    req_data = request.get_json()
    print(req_data)
    project = Project(req_data['title'], req_data['userId'], req_data['description'], req_data['totalCost'], req_data['totalTime'])
    
    db.session.add(project)
    db.session.commit()
    result = project_schema.dump(project)
    print(result)
    return jsonify(result.data)

@routes.route('/project/<projectId>')
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

@routes.route('/delete_project/<projectId>', methods=['DELETE'])
def delete_project(projectId):
    projectItems = ProjectItem.query.filter_by(projectId=projectId)
    for projectItem in projectItems:
        db.session.delete(projectItem)
        db.session.commit()

    project = Project.query.filter_by(id=projectId).first()
    db.session.delete(project)
    db.session.commit()
    return '', 204