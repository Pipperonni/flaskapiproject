from . import bp as auth_bp
from app.forms import RegisterForm, SignInForm
from app.blueprints.collect.models import User
from flask_login import login_user, logout_user, login_required
from flask import render_template, redirect, flash

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username=form.username.data
        email=form.email.data
        password=form.password.data
        u = User(username=username, email=email, password_hash='')
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:  
            flash(f'{username} already exists, please try again.')
            return redirect('/')
        elif email_match:
            flash(f'{email} already exists, please try again.')
            return redirect('/')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Request to register {username} successful')
            return redirect('/register')
    return render_template('/register.jinja', form=form)

@auth_bp.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = SignInForm()
    username = form.username.data
    password = form.password.data
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username or password are incorrect, try again')
            return redirect('/')
        flash(f'{username} successfully signed in')
        login_user(user_match, remember=form.remember_me.data)
        return redirect('/')    
    return render_template('/sign_in.jinja', form=form)

@auth_bp.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect('/')