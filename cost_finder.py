import requests
import json
import time
import math
import hmac
import hashlib
import ast
import os
from find_server_time import BinanceTime

class CostFinder:
    def __init__(self, symbol):
        super().__init__()
        
        base_url = 'https://api.binance.com/api/v3/myTrades?'

        symbol = f'symbol={symbol}'
        limit = 'limit=500'
        ts = BinanceTime()
        timestamp = f'timestamp={ts()}'

        query_string = f'{symbol}&{limit}&{timestamp}'
        secret = os.environ["binance_secret_key"]
        signature = f'signature={self.hashing(secret, query_string)}'

        self.url = f'{base_url}{query_string}&{signature}'
        
        self.payload={}
        self.headers = {
            'Content-Type': 'application/json',
            'X-MBX-APIKEY': os.environ["binance_api_key"]
        }

    def hashing(self, secret, query_string):
        return hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    def find_cost(self, d: list) -> int:
        cost = 0
        qty = 0
        for item in d:
            item['qty'] = float(item['qty'])
            item['price'] = float(item['price'])

            price = item['qty'] * item['price']
            if item['isBuyer']:
                cost += price
                qty += item['qty']
            else:
                cost -= price
                qty -= item['qty']
    
        avgCost = cost / qty

        return avgCost, cost, qty

    def __call__(self):

        response = requests.request('GET', self.url, headers=self.headers, data=self.payload)
        data = response.text
        data = data.replace('true', 'True').replace('false', 'False')
        d = ast.literal_eval(data)

        return self.find_cost(d)

if __name__ == '__main__':
    symbol = input("Enter Symbol (Ex: ETHUSDT or ADAUSDT): ")
    cost_finder = CostFinder(symbol)
    avgCost, cost, qty = cost_finder()

    print(f'Average Cost: {avgCost}\nCost: {cost}\nQuantity: {qty}')
