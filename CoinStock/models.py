from flask_login import UserMixin
from datetime import datetime
from CoinStock import loginmanager, db


@loginmanager.user_loader
def load_user(id):
    return User.query.get(id)

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    interest = db.relationship('Interest', backref='user', lazy=True)

    def __repr__(self) -> str:
        return "Id: {}, Name: {}, Email: {}".format(self.id, self.name, self.email)


class Interest(db.Model):
    """
      interest table stores stocks, cryptocurrencies user is interested in.
      i_type - stores the type of interest ['stock', 'crypto', 'efts', etc]
      i_name - stores the name of interest ['AAPL', 'Bitcoin', etc]
    """
    interest_id = db.Column(db.Integer, primary_key=True)
    i_type = db.Column(db.String(20), nullable=False)
    i_name = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    user_id = db.Column(db.Integer,  db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self) -> str:
        return "Id: {}, Type: {}, Name: {}, User_id: {}".format(self.id, self.i_type, self.i_name, self.user_id)