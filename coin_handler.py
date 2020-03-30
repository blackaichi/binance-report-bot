filepath = "coins"

def add_coin(coin, ID):
    with open(filepath, 'a') as fd:
        fd.write(ID + " "*(5-len(ID)) + "= '" + coin + "'\n")