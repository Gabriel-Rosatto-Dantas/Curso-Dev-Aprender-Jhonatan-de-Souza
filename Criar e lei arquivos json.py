import json
#criar ou ler um arquivo json existente(primeiro criar em formato de string )
computador_json = '''{
    "marca": "Dell",
    "preço": 15000
}'''
#para transformar essa string em um arquivo json
#ler direto apartir da varável("loads" transforma uma string em dicionário))
data = json.loads(computador_json)
print(data["preço"])

#Agora para criar um arquivo json que seja salvo no computador(Salvar um string JSON -> arquivo JSON)
with open('computador.json','w', encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json)

#para ler um arquivo JSoN
with open('computador.json', encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json)#convertendo o JSON -> para uma string
    dicionario_computador_json = json.loads(string_computador_json)#converter de string -> Dicionário python
    print(dicionario_computador_json["marca"])

#desafio
##criar uma arquivo json
usuarios_json = '''{
    "name": "John Smith",
    "age": 30,
    "city": "New York",
    "isStudent": true,
    "gpa": 3.5
}'''
##Atenção ao criar o arquivo json no "w"(de write)
with open('desafio.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(usuarios_json, arquivo_json)
