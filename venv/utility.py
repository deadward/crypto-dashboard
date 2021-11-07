# import modules
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class ApiUtil:
    # get coin prices based on symbols passed in
    @staticmethod
    def coin_price(coin_list):
        # build symbol list based on list of dictionaries
        symbols = ""
        for i in coin_list:
            if symbols == "":
                symbols = i["symbol"]
            else:
                symbols = symbols + "," + i["symbol"]

        # coinmarketcap API
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
            'symbol': symbols,
        }
        # API_KEY is from the dev account on coinmarketcap, replace the x's
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    # pull out relevant data from the json return
    @staticmethod
    def parse_json(dump):
        result_list = []
        for i in dump["data"]:
            for j, k in dump["data"][i].items():
                if j == "quote":
                    for l, m in k.items():
                        result_dict = {"symbol": i, "price": m["price"], "percent_change_24h": m["percent_change_24h"]}
                        result_list.append(result_dict)
        return result_list


class CoinUtil:
    # create dictionary with coins, amounts, and cost
    # it is important to note that symbols must be capitalized and match exactly what coinmarketcap shows
    @staticmethod
    def create_coin_dict():
        coin_list = [
            {"symbol": "IQ", "amount": 250000, "cost": 3000},
            {"symbol": "ETH", "amount": 2, "cost": 4500},
            {"symbol": "VET", "amount": 5000, "cost": 500},
            {"symbol": "LINK", "amount": 40, "cost": 1000},
            {"symbol": "SC", "amount": 30000, "cost": 500},
            {"symbol": "ONE", "amount": 4000, "cost": 1000},
            {"symbol": "MOON", "amount": 800, "cost": 0},
            {"symbol": "BTC", "amount": .2, "cost": 8000},
            {"symbol": "VTHO", "amount": 400000, "cost": 3000},
            {"symbol": "ADA", "amount": 2300, "cost": 4000},
            {"symbol": "COMP", "amount": 1.5, "cost": 500},
            {"symbol": "ELON", "amount": 500000000, "cost": 100},
            {"symbol": "SMI", "amount": 40000000, "cost": 250}
        ]
        return coin_list

    # calculate crypto value, total gain/loss percentage, and portfolio distribution
    @staticmethod
    def calc_value(coin, dump):
        new_list = []
        total_value = 0
        for i in dump:
            for j in coin:
                if i["symbol"] == j["symbol"]:
                    value = round(i["price"] * j["amount"], 2)
                    if j["cost"] is not 0:
                        total_change = (value / j["cost"] - 1) * 100
                    else:
                        total_change = 0
                    new_list.append({"symbol": j["symbol"], "amount": j["amount"], "price": i["price"], "value": value,
                                     "percent_change_24h": round(i["percent_change_24h"], 2), "total_change": round(total_change, 2)})
                    total_value = total_value + value

        # calculating portfolio distribution per coin and adding it to the dictionary for said coin
        for k in new_list:
            diversity = round(k["value"] / total_value * 100, 2)
            k["diversity"] = diversity

        return new_list
