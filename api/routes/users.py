from flask import Blueprint

from . import routes

from app import db
from app import User
from app import user_schema
from app import users_schema

from flask import jsonify
from sqlalchemy.sql import func
from flask import render_template, url_for, request, redirect

@routes.route('/')
def index():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result.data)

@routes.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    username = request.form['username']
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(username=username).first()
    result = user_schema.dump(user)
    return jsonify(result.data)

@routes.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    result = user_schema.dump(user)
    return jsonify(result.data)