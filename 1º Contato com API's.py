# Como usar 4 principais comandos(verbos) de uma API

import requests
from pprint import pprint

#Get

resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

resultado_get_por_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
#pprint(resultado_get_por_id.json())

# POST - Criar um novo recurso

nova_tarefa = {'completed': False,
 'title': 'Lavar o carro',
 'userId': 1}

resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos/2', nova_tarefa)
#pprint(resultado_post.json())

#PUT - Alterar um recurso existente

tarefa_alterada = {'completed': False,
 'title': 'Lavar moto',
 'userId': 1}

resultado_tarefa_alterada = requests.put('https://jsonplaceholder.typicode.com/todos/2', tarefa_alterada)
#pprint(resultado_tarefa_alterada.json())

#Delete - Ecluir um recurso

resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())
