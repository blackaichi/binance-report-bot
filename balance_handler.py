import json
from binance.client import Client

filepath = "coins_on_balance.json"

def get_balance():
    print("ei")

def search_coins(client):
    info = client.get_account()
    a = {}
    for i in info['balances']:
        if i['free'] != '0.00000000' or i['locked'] != '0.00000000':
            a[i['asset']] = float(i['free']) + float(i['locked'])
    return a

def write_coins(coins):
    with open(filepath, 'w+') as fd:
        a = []
        for i in coins.keys():
            a.append(i)
        print(a)
        json.dump(a,fd)
