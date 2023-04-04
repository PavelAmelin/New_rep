import json
result = {'orders': []}

def write_order_to_json(item, quantity, price, buyer, date):
    result['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})
    with open('orders.json', 'w', encoding='utf-8') as out:
        json.dump(result, out, indent=4, ensure_ascii=False)

write_order_to_json("принтер", "10", "6700", "Ivanov I.I.", "24.09.2017")
write_order_to_json("scaner", "20", "10000", "Petrov P.P.", "11.01.2018")
write_order_to_json("scaner", "20", "10000", "Petrov P.P.", "11.01.2018")
write_order_to_json("scaner", "20", "10000", "Petrov P.P.", "11.01.2018")