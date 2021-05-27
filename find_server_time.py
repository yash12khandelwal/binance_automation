import requests
import json
import ast
import re

class BinanceTime:
    def __init__(self):
        super().__init__()
        self.url = 'https://api.binance.com/api/v3/time'
        self.payload={}
        self.headers = {
                'Content-Type': 'application/json'
        }

    def __call__(self):

        response = requests.request('GET', self.url, headers=self.headers, data=self.payload)

        x = ast.literal_eval(response.text)
        return x['serverTime']

if __name__ == '__main__':
    binance_time = BinanceTime()
    print(binance_time())
