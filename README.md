# crypto-dashboard
 Dashboard to track crypto prices and change via the coinmarketcap APIs. Uses chart.js and ag-grid. 

Requirements: 
python 3 (was written in 3.8.2 but probably any verison of 3 will work) 
pycharm community edition (you could probably use idle as well but you need to get the html file in the proper folder structure) 
pip install flask 
pip install requests

Create a basic dev account on https://coinmarketcap.com/api/ to get an API key. (It is free and you get 10,000 credits a month. This app only uses 1 credit every time it loads)

General: 
You need to update the API key in coin_price() in utility.py file 
You need to update your symbols and amounts in create_coin_dict() in utility.py 
The app runs locally at http://127.0.0.1:5000 (it should show once you run app.py)
