from flask import Blueprint, render_template, redirect

from CoinStock.Markets.forms import CoinForm
from CoinStock.Markets.coins import CoinsData 
from CoinStock.Markets.stocks import StockData

main = Blueprint('Main', __name__)


@main.route('/', methods=['POST','GET'])
def index():
    coins = CoinsData()
    form = CoinForm()
    data = None
    popular_coins = coins.popular_coins
    if form.validate_on_submit():
        coin_name = form.coin_name.data.lower()
        currency = form.currency.data.lower()

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