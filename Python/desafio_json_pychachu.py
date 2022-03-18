from importlib.resources import path
import json
from pathlib import Path
arquivo_json_pikachu = Path("pikachu.json").read_text()
arquivo_json = json.loads(arquivo_json_pikachu)
print(arquivo_json["abilities"][1]["ability"]["name"])
