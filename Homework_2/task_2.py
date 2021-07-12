import json


def write_order_json(item, quantity, price, buyer, date):
    product = {'item': item,
               'quantity': quantity,
               'price': price,
               'buyer': buyer,
               'date': date}
    with open('orders.json', 'r', encoding='utf-8') as data_json:
        data_file = data_json.read()
        data_to_write = json.loads(data_file)
        data_to_write['orders'].append(product)
    with open('orders.json', 'w', encoding='utf-8') as json_write:
        json_write.write(json.dumps(data_to_write, indent=4, ensure_ascii=False))

write_order_json('Python Professional', 25, 900, 'Sergey', '20.06.2021')
write_order_json('Путь Python', 50, 1500, 'Джульен Данжу', '20-06-2021')