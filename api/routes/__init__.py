from flask import Blueprint
routes = Blueprint('routes', __name__)

from .projectItems import *
from .projects import *
from .users import *