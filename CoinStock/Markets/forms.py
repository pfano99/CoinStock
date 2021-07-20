from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, SelectField


class CoinForm(FlaskForm):
    coin_name = StringField('Coin Name', validators=[DataRequired()] )
    currency = SelectField('Currency', validators=[DataRequired()], choices=['ZAR', 'USD', 'EUR'])
    submit = SubmitField('Search')

class StockForm(FlaskForm):
    symbol = StringField('Stock Symbol', validators=[DataRequired()] )
    interval = SelectField('interval', validators=[DataRequired()], choices=[ '1min', '5min', '30min', '1h', '2h', '1day', '1week', '1month' ])
    submit = SubmitField('Search')
