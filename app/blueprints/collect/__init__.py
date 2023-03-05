from flask import Blueprint

bp = Blueprint('collect', __name__, url_prefix='/collect')

from . import routes, models