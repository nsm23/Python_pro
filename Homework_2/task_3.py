import yaml

data = {
    'items': ['computer', 'printer', 'keyboard', 'mouse'],
    'items_quantity': 4,
    'items_price': {
        'system blok': '45000rub.-150 000rub.',
        'keyboard': '199rub.-3000rub.',
        'mouse': '299rub.-1500rub.',
        'printer': '3500rub.-17 000rub.'
    }
}

with open('test.yaml', 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)

with open('test.yaml') as f_n:
    print(f_n.read())