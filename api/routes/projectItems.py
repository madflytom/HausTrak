from flask import Blueprint

from . import routes

from app import db
from app import ProjectItem
from app import projectItems_schema
from app import projectItem_schema

from flask import jsonify
from flask import render_template, url_for, request, redirect

@routes.route('/projectItem')
def projectItems():
    projectItems = ProjectItem.query.all()
    result = projectItems_schema.dump(projectItems)
    return jsonify(result.data)

@routes.route('/projectItem/<projectId>')
def getProjectItemsForProject(projectId):
    projectItems = ProjectItem.query.filter_by(projectId=projectId)
    result = projectItems_schema.dump(projectItems)
    return jsonify(result.data)

@routes.route('/post_projectItem', methods=['POST'])
def post_projectItem():
    req_data = request.get_json()
    projectItem = ProjectItem(req_data['title'], req_data['projectId'], req_data['description'], req_data['cost'], req_data['time'], req_data['done'])
    db.session.add(projectItem)
    db.session.commit()
    result = projectItem_schema.dump(projectItem)
    return jsonify(result.data)

@routes.route('/check_projectItem/<projectItemId>', methods=['POST'])
def check_projectItem(projectItemId):
    projectItem = ProjectItem.query.filter_by(id=projectItemId).first()
    req_data = request.get_json()
    done = req_data['done']
    projectItem.done = done
    db.session.commit()
    result = projectItem_schema.dump(projectItem)
    return jsonify(result.data)

@routes.route('/delete_projectItem/<projectItemId>', methods=['DELETE'])
def delete_projectItem(projectItemId):
    projectItem = ProjectItem.query.filter_by(id=projectItemId).first()
    db.session.delete(projectItem)
    db.session.commit()
    return '', 204