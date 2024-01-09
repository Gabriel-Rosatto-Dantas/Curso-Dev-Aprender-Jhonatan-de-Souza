#Imprimir o e-mail do usuario com id 2
#Imprimir a city do usuario com id 1
#Imprimir o total do pedido do usuario com id 2

import json

with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter arquivo json para string
    print(data["user"][1]["email"])
    print(data["user"][0]["address"]["city"])
    print(data["user"][1]["orders"][0]["total"])
