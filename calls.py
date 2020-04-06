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

a = 0
last_btc = 1
last_busd = 1

def get_coin(coin):
    info = client.get_avg_price(symbol=coin)
    send_message(coin, info["price"])

def get_all_coins_on_balance():
    values = balance_handler.get_value_coins(client)
    for i,v in values.items():
        send_message(i, v)

def get_all_coins():
    c = coin_handler.get_IDs()
    for i in c:
        info = client.get_avg_price(symbol=i)
        send_message(i, info["price"])

def send_message(coin, price):
    bot.send_message(chat_id = bot_chatID, text = str(coin) + ": " + str(price) + " $")

def execute():
    #calculate balance and say hello
    coins = balance_handler.search_coins(client)
    balance_handler.write_coins(coins)
    if a == 0:
        bot.send_message(chat_id = bot_chatID, text = "Bon dia, aqui tens el teu report matinal:")
        a = 1
    else:
        bot.send_message(chat_id = bot_chatID, text = "Bon dia, aqui tens el teu report nocturn:")
        a = 0
    btc = balance_handler.get_balance(client, coins)
    bot.send_message(chat_id = bot_chatID, text = "Total balance: " + str(btc) + " B\n")
    busd = client.get_avg_price(symbol='BTCBUSD')
    busd = float(busd['price'])*btc
    bot.send_message(chat_id = bot_chatID, text = "Total balance: " + str(busd) + " $\n")

    # calculate profit
    bot.send_message(chat_id = bot_chatID, text = "Profit last 12h: " + str((float(last_btc)/btc)*100) + " %\n")
    bot.send_message(chat_id = bot_chatID, text = "Profit last 12h: " + str((float(last_busd)/busd)*100) + " %\n")

    # calculate price of all coins on wallet
    get_all_coins_on_balance()

    # calculate price of all coins selected
    get_all_coins()
    last_btc = btc
    last_busd = busd

schedule.every().day.at("10:00").do(execute)
schedule.every().day.at("22:00").do(execute)


while True:
    schedule.run_pending()
    time.sleep(60)
