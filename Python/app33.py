import requests
from pprint import pprint

# Get
resultado_get = requests.get("https://jsonplaceholder.typicode.com/todos")
# pprint(resultado_get.json())

# Get com id

resultado_get_com_id = requests.get(
    "https://jsonplaceholder.typicode.com/todos/2")
# pprint(resultado_get_com_id.json())

# POST - Criar um novo recurso
nova_tarefa = {'completed': False,
               'id': 2,
               'title': 'lavar o carro',
               'userId': 1}
resultado_post = requests.post(
    "https://jsonplaceholder.typicode.com/todos", nova_tarefa)
pprint(resultado_post.json())
# PUT Alterar um recurso existente
tarefa_aterada = {'completed': False,
                  'id': 2,
                  'title': 'lavar a moto',
                  'userId': 1}

resultado_put = requests.put(
    "https://jsonplaceholder.typicode.com/todos/2", tarefa_aterada)
pprint(resultado_put.json())

# DELETE - Excluir um recurso

resultado_delete = requests.delete(
    "https://jsonplaceholder.typicode.com/todos/2")
pprint(resultado_delete.json())
