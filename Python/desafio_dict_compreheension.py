# Dictionary compreheension
# [expressão for membro in iterável] - list
# {chave:expressão for membro in iterável} - dict
from pprint import pprint
import random
sorteios = ["sorteio 1", "sorteio 2", "sorteio 3"]
participantes = ["joel", "jessica", "maria",
                 "cris", "larissa", "rafael", "marcus", "john"]

# sorteado = participantes[random.randint(0, len(participantes) - 1)]
# sorteado = random.choices(participantes)
pprint({sorteio: participantes[random.randint(0, len(participantes) - 1)]
        for sorteio in sorteios})

pprint({sorteio: random.choice(participantes)
       for sorteio in sorteios})  # forma mais facil com choices

grupos = ["grupo 1", "grupo 2", "grupo 3"]

pprint({grupo: [random.randint(1, 101) for i in range(5)] for grupo in grupos})
