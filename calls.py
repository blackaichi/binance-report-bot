from binance.client import Client
import constants
import json
import telegram
import requests
import schedule
import time
import coin_handler
import balance_handler

f = open("keys.json", "r").read()
keys = json.loads(f)

public_key = keys["public"]
private_key = keys["private"]
bot_token = keys["token"]
bot_chatID = keys["chatID"]
client = Client(public_key, private_key)
bot = telegram.Bot(token=bot_token)

def get_coin(coin):
    info = client.get_avg_price(symbol=coin)
    send_message(coin, info["price"])

def get_all_coins():
    c = coin_handler.get_IDs()
    balance_handler.get_balance()
    for i in c:
        info = client.get_avg_price(symbol=i)
        send_message(i, info["price"])

def send_message(coin, price):
    bot.send_message(chat_id = bot_chatID, text = coin + ": " + price)

#get_all_coins()
a = balance_handler.search_coins(client)
balance_handler.write_coins(a)
#info = client.get_account()
#print(info)
"""
schedule.every().day.at("10:00").do(get_all_coins)
schedule.every().day.at("22:00").do(get_all_coins)
a = 0;
while True:
    if a == 0:
        info = client.get_account()
        balance_handler.search_coins(client)
        balance_handler.write_coins()
        bot.send_message(chat_id = bot_chatID, text = Bon dia aqui tens el teu report matinal:)
    else 
        bot.send_message(chat_id = bot_chatID, text = Bon dia aqui tens el teu report nocturn:)
    #get_all_coins()
    schedule.run_pending()
    time.sleep(60)
"""