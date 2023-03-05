from . import bp as main_bp
from flask import render_template

@main_bp.route('/')
def index():
    return render_template('index.jinja')

@main_bp.route('/about')
def about():
    return render_template('about.jinja')