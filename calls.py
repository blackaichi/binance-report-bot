from binance.client import Client
import constants
import json
import telegram
import requests
import schedule
import time
import coin_handler

f = open("keys", "r").read()
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
    info = client.get_avg_price(symbol=constants.ALGO)
    send_message(constants.ALGO, info["price"])

def send_message(coin, price):
    bot.send_message(chat_id = bot_chatID, text = coin + ": " + price)

"""
schedule.every().day.at("10:00").do(get_all_coins)
schedule.every().day.at("22:00").do(get_all_coins)
"""

coin_handler.add_coin("BTCEUR", "BTC")
get_all_coins()
"""
while True:
    #get_all_coins()
    schedule.run_pending()
    time.sleep(60)
"""