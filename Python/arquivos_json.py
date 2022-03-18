# JavaScript object notetion JSON
from importlib.resources import path
import json
from pathlib import Path

carros = [
    {"marca": "nissan", "preco": 45.000, "cor": "azul"},
    {"marca": "ford", "preco": 75.000, "cor": "verde"},
    {"marca": "bmw", "preco": 117.000, "cor": "amarelo"}
]
carros_json = json.dumps(carros)
Path("carros.json").write_text(carros_json)

arquivo_carro_json = Path("carros.json").read_text()
arquivo_json = json.loads(arquivo_carro_json)
print(arquivo_json[0]["marca"] + " " + str(arquivo_json[0]["preco"]))
print(arquivo_json[1]["marca"] + " " + str(arquivo_json[1]["preco"]))
