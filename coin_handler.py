import json

filepath = "coins.json"

def add_coin(name, ID):
    with open(filepath, 'r+') as fd:
        data = json.load(fd)
        d = {name : ID}
        data.update(d)
        fd.seek(0)
        json.dump(data, fd)

def get_all_coins():
    with open(filepath, 'r') as fd:    
        data = json.load(fd)
        a = {}
        for i,v in data.items():
            a[i] = v

def get_IDs():
    with open(filepath, 'r') as fd:    
        data = json.load(fd)
        a = []
        for v in data.values():
            a.append(v)
        return a