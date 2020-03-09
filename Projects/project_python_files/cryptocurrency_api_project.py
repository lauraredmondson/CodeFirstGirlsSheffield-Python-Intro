
from pprint import pprint
from requests import Session
import json
import os

api_key = os.environ.get("crypto_api_key")

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '2', # number of returned coins from the request
    'convert': 'USD' # currency the value is returned in
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
crypto_dict = json.loads(response.text)['data']
pprint(crypto_dict)

# print the names of all the coins and their value
for coin in crypto_dict:
    coin_price_usd = coin['quote']['USD']['price'] # get the value in USD
    print('{} is worth ${:.2f}'.format(coin['name'], coin_price_usd)) # print the value in USD
