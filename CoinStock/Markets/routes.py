from flask import Blueprint, render_template

from CoinStock.Markets.stocks import StockData
from CoinStock.Markets.forms import StockForm
from CoinStock.Markets.coins import CoinsData 

market = Blueprint('Market', __name__)



@market.route('/stocks', methods=['POST', 'GET'])
def stocks():
    data = None
    form = StockForm()
    stocks = StockData()
    if form.validate_on_submit():
        name = form.symbol.data 
        interval = form.interval.data
        data = stocks.get_stock(symbol=name, interval=interval)

        return render_template('stocks.html', data=data, form=form)
        
    return render_template('stocks.html', data=data, form=form)