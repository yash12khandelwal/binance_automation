# binance_automation

## Find server time

This file is used to find the binance server time as for any get or post request, timestamp is also sent with the request.
Timestamp should be within 1000ms range of the binance server timestamp.
This file gets the binance server timestamp, which can be used for calling other APIs.

## Find Average Cost

Binance sadly doesn't give an estimate of what's my average cost of buying a particular asset. Most people buy asset at many dips and they lose track of what's my average cost.
This script will easily calculate your average cost.

This file requires your Binance API Key and Binance Secret Key which are used as an environment variable binance_api_key and binance_secret_key.
You can get the API Key and Secret Key from your Binance Account. Pass them as enviornment variable or replace it the code.

Command to run the file: `python3 cost_finder.py`.

You will get a prompt to enter the symbol. Example of symbol are `ETHUSDT` or `BNBUSDT` or `ADABUSD` etc.

### More functionalities will be added soon
