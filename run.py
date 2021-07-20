# from flask import Flask, render_template, jsonify, redirect, url_for, flash
# from flask_login import login_required, current_user, logout_user, UserMixin, LoginManager
# from flask_bcrypt import Bcrypt
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import backref
# from datetime import date, datetime

# from coins import CoinsData
# from stocks import StockData
# from secrets_info import secret_key

# from forms import CoinForm, StockForm, LoginForm, SignupForm, InterstForm

# app = Flask(__name__)
# app.config['SECRET_KEY'] = secret_key
# app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'

# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
# loginmanager = LoginManager(app)

# @loginmanager.user_loader
# def load_user(id):
#     return User.query.get(id)

# class User(db.Model, UserMixin):
#     user_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(150), nullable=False)
#     password = db.Column(db.String(20), nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
#     interest = db.relationship('Interest', backref='user', lazy=True)

#     def __repr__(self) -> str:
#         return "Id: {}, Name: {}, Email: {}".format(self.id, self.name, self.email)


# class Interest(db.Model):
#     """
#       interest table stores stocks, cryptocurrencies user is interested in.
#       i_type - stores the type of interest ['stock', 'crypto', 'efts', etc]
#       i_name - stores the name of interest ['AAPL', 'Bitcoin', etc]
#     """
#     interest_id = db.Column(db.Integer, primary_key=True)
#     i_type = db.Column(db.String(20), nullable=False)
#     i_name = db.Column(db.String(50), nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
#     user_id = db.Column(db.Integer,  db.ForeignKey('user.user_id'), nullable=False)

#     def __repr__(self) -> str:
#         return "Id: {}, Type: {}, Name: {}, User_id: {}".format(self.id, self.i_type, self.i_name, self.user_id)


# @app.route('/', methods=['POST','GET'])
# def index():
#     coins = CoinsData()
#     form = CoinForm()
#     data = None
#     popular_coins = coins.popular_coins
#     if form.validate_on_submit():
#         coin_name = form.coin_name.data.lower()
#         currency = form.currency.data.lower()

#         # data = ['name', 'last name']
#         data = coins.coin_data(coin_name, currency)
        
#         coin_info = {}
#         if data:
#             coin_image = data['image']
#             try:
#                 data = data[coin_name]
#             except KeyError:
#                 data = data[ "".join(coin_name.split(' ')) ]
#             except:
#                 data = data[ '-'.join(coin_name.split(' '))]
                
#             coin_info['name'] = coin_name
#             coin_info['price'] = data[currency]
#             coin_info['currency'] = currency
#             coin_info['market_cap'] = round(data[ "{}_market_cap".format(currency.lower()) ], 2)
#             coin_info['vol'] = round(data[ "{}_24h_vol".format(currency.lower()) ], 2)
#             coin_info['change'] = round(data[ "{}_24h_change".format(currency.lower()) ], 2)
#             coin_info['image'] = coin_image

#         return render_template('index.html', popular_coins=popular_coins, data=coin_info, form=form)
#     return render_template('index.html', popular_coins=popular_coins, data=data, form=form)


# @app.route('/stocks', methods=['POST', 'GET'])
# def socks():
#     data = None
#     form = StockForm()
#     stocks = StockData()
#     if form.validate_on_submit():
#         name = form.symbol.data 
#         interval = form.interval.data
#         data = stocks.get_stock(symbol=name, interval=interval)

#         return render_template('stocks.html', data=data, form=form)
        
#     return render_template('stocks.html', data=data, form=form)


# @app.route('/test/')
# def test():
#     stocks = StockData()
#     data = stocks.clean_data()

#     return jsonify(data)


# @app.route('/signup/', methods=['POST', 'GET'])
# def signup():
#     form = SignupForm()
#     title="Signup"
#     if form.validate_on_submit():
#         user = User(
#             name = form.name.data,
#             email = form.email.data,
#             password = bcrypt.generate_password_hash(form.password.data)
#         )
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('login'))
#     return render_template('signup.html', form=form, title=title)


# @app.route('/login/', methods=['POST', 'GET'])
# def login():
#     form = LoginForm()
#     title="Login"
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and user.password == bcrypt.check_password_hash(form.password.data):
#             login(user) 
#     return render_template('login.html', form=form, title=title)


# @app.route('/add-interests/', methods=['POST', 'GET'])
# @login_required
# def add_interest():
#     form = InterstForm()
#     title = "New interest"
#     if form.validate_on_submit():
#         interst = InterstForm(
#             user_id = current_user.id,
#             i_type = form.i_type.data,
#             i_name = form.i_name.data,
#             currency = form.currency.data
#         )
#         db.session.add(interst)
#         db.session.add()
#         flash('New Interest have been successfully added', 'success')
#         return  redirect(url_for('dashboard'))
#     return render_template('add_interest.html', form=form, title=title)


# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html')

from CoinStock import app

if __name__=='__main__':
    app.run(debug=True)




