import yaml

result = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
          'items_quantity': 4,
          'items_price': {'computer': '200€-1000€', 'keyboard': '5€-50€', 'mouse': '4€-7€', 'printer': '100€-300€'}
          }

with open('file.yaml', 'w', encoding='utf-8') as out:
    yaml.dump(result, out, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r', encoding='utf-8') as inp:
    cont = yaml.load(inp, Loader=yaml.FullLoader)
    print(cont)
