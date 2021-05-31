from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'ferrari', 'price': 15000},
        {'id': 2, 'name': 'Aston Martin', 'price': 20000},
        {'id': 3, 'name': 'Mercedes', 'price': 18000}
    ]
    return render_template('market.html', items=items)
