from typing import final
from flask import Flask, json, render_template, jsonify

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, SelectField

from coins import CoinsData


app = Flask(__name__)
app.config['SECRET_KEY'] = 'THEKEY'

class CoinForm(FlaskForm):
    coin_name = StringField('Coin Name', validators=[DataRequired()] )
    currency = SelectField('Currency', validators=[DataRequired()], choices=['ZAR', 'USD', 'EUR'])
    submit = SubmitField('Search')

@app.route('/', methods=['POST','GET'])
def index():
    coins = CoinsData()
    form = CoinForm()
    data = None
    popular_coins = coins.popular_coins
    if form.validate_on_submit():
        coin_name = form.coin_name.data.lower()
        currency = form.currency.data.lower()

        # data = ['name', 'last name']
        data = coins.coin_data(coin_name, currency)
        
        coin_info = {}
        if data:
            coin_image = data['image']
            try:
                data = data[coin_name]
            except KeyError:
                data = data[ "".join(coin_name.split(' ')) ]
            except:
                data = data[ '-'.join(coin_name.split(' '))]
                
            coin_info['name'] = coin_name
            coin_info['price'] = data[currency]
            coin_info['currency'] = currency
            coin_info['market_cap'] = round(data[ "{}_market_cap".format(currency.lower()) ], 2)
            coin_info['vol'] = round(data[ "{}_24h_vol".format(currency.lower()) ], 2)
            coin_info['change'] = round(data[ "{}_24h_change".format(currency.lower()) ], 2)
            coin_info['image'] = coin_image

        return render_template('index.html', popular_coins=popular_coins, data=coin_info, form=form)
    return render_template('index.html', popular_coins=popular_coins, data=data, form=form)

@app.route('/test/')
def test():
    coins = CoinsData()
    data = coins.coin_data('bitcoin', 'ZAR')
    # data = coins.popular_coins

    # return render_template('results.html')
    return jsonify(data)


if __name__=='__main__':
    app.run(debug=True)




