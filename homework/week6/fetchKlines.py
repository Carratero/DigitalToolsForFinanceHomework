#!/Users/antonincarratero/opt/anaconda3/bin/python

from binance.client import Client 
client = Client(api_key, api_secret, testnet=True)

# Get server timestamp
print(client.time())
# Get klines of BTCUSDT at 1m interval
print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
print(client.klines("BNBUSDT", "1h", limit=10))

klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
