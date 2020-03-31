import json
from binance.client import Client

filepath = "coins_on_balance.json"

def get_balance(client, a):
    btc = 0
    for i,v in a.items():
        if i != 'BTC':
            prize = client.get_avg_price(symbol=i+'BTC')
            btc += float(prize['price'])*float(v)
        else:
            btc += float(v)
    return btc

def search_coins(client):
    info = client.get_account()
    a = {}
    for i in info['balances']:
        if i['free'] != '0.00000000' or i['locked'] != '0.00000000':
            a[i['asset']] = float(i['free']) + float(i['locked'])
    return a

# writes coins on coins_on_balance.json
def write_coins(coins):
    with open(filepath, 'w+') as fd:
        a = []
        for i in coins.keys():
            a.append(i)
        json.dump(a,fd)

def get_value_coins(client):
    with open(filepath, 'r') as fd:
        data = json.load(fd)
        a = {}
        for i in data:
            if i != 'BTC':
                prize = client.get_avg_price(symbol=i+'BTC')
                prize2 = client.get_avg_price(symbol='BTCBUSD')
                a[i] = float(prize['price'])*float(prize2['price'])
            else:
                a[i] = client.get_avg_price(symbol=i+'BUSD')
        return a