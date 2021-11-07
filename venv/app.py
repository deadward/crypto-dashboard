# importing modules
from flask import Flask, render_template
from utility import ApiUtil, CoinUtil
from operator import itemgetter

# declaring app name
app = Flask(__name__)

# defining home page
@app.route('/')
def homepage():
    # creates a list of dictionaries, enriches the list with data from CMC, calculates values, % change, and distribution
    stonks = main()
    # sorting by value so donut chart shows correctly
    sorted_stonks = sorted(stonks, key=itemgetter('value'), reverse=True)
    # returning index.html
    return render_template("index.html", stonks=sorted_stonks)

# main method (what a comment)
def main():
    # creates list of symbols and relevant data
    coin_list = CoinUtil.create_coin_dict()
    # get coin prices and add to the list
    dump = ApiUtil.coin_price(coin_list)
    # pull out relevant data from CMC API call
    dump_list = ApiUtil.parse_json(dump)
    # combines lists in the proper format for chart.js and ag-grid for the UI
    coin_list_final = CoinUtil.calc_value(coin_list, dump_list)
    return coin_list_final

# running app
app.run(use_reloader=True, debug=True)