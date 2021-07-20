
from flask import Blueprint, render_template, redirect, url_for
from flask_login import logout_user, login_user


from CoinStock import db, bcrypt
from CoinStock.Auth.forms import LoginForm, SignupForm
from CoinStock.models import User

auth = Blueprint('Auth', __name__)


@auth.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    title="Signup"
    if form.validate_on_submit():
        user = User(
            name = form.name.data,
            email = form.email.data,
            password = bcrypt.generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('Auth.login'))
    return render_template('signup.html', form=form, title=title)


@auth.route('/login/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    title="Login"
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == bcrypt.check_password_hash(form.password.data):
            login(user) 
            return redirect(url_for('User.dashboard'))
    return render_template('login.html', form=form, title=title)

    
@auth.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('Main.index'))