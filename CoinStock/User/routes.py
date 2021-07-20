from flask import Blueprint, url_for, render_template, redirect, flash, jsonify
from flask_login import login_required, current_user
from CoinStock.User.forms import InterstForm

from CoinStock import db 
from CoinStock.Markets.coins import CoinsData
from CoinStock.Markets.stocks import StockData

user = Blueprint('User', __name__)


@user.route('/add-interests/', methods=['POST', 'GET'])
@login_required
def add_interest():
    form = InterstForm()
    title = "New interest"
    if form.validate_on_submit():
        interst = InterstForm(
            user_id = current_user.id,
            i_type = form.i_type.data,
            i_name = form.i_name.data,
            currency = form.currency.data
        )
        db.session.add(interst)
        db.session.add()
        flash('New Interest have been successfully added', 'success')
        return  redirect(url_for('dashboard'))
    return render_template('add_interest.html', form=form, title=title)


@user.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@user.route('/test/')
def test():
    stocks = StockData()
    data = stocks.clean_data()

    return jsonify(data)








