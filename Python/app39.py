# Dictionary compreheension
# [expressão for membro in iterável] - list
# {chave:expressão for membro in iterável} - dict
import random
from pprint import pprint
pprint({i: i for i in range(10)})
# popular um dicionario com valores de outra lista base
produtos = ["produto 1", "produto 2", "produto 3", "produto 4", "produto 5"]
pprint({produto: 1 for produto in produtos})
# Gerar uma matriz de valores de teste
pprint({produto: [7 for i in range(5)] for produto in produtos})
# [expressão for membro in iterável]
pprint({produto: [i * 2 for i in range(5)] for produto in produtos})
# Gera valores de teste usando Random
pprint({produto: [random.randint(1, 61)
       for i in range(5)] for produto in produtos})
