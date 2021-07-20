from flask import Flask, render_template, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user, UserMixin, LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


from CoinStock.secrets_info import secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'

bcrypt = Bcrypt(app)
loginmanager = LoginManager(app)
db = SQLAlchemy(app)

from CoinStock.User.routes import user
from CoinStock.Auth.routes import auth
from CoinStock.Markets.routes import market
from CoinStock.Main.routes import main

app.register_blueprint(auth)
app.register_blueprint(market)
app.register_blueprint(user)
app.register_blueprint(main)




# from models import * 