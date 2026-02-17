import json

pessoa = {
    "nome": "Daniel",
    "idade": 50,
    "altura": 1.76,
    "dev": True,
    "linguagens": ["Python", "Java", "Go"]
}

with open("pessoa.json", "w") as arquivo_json:
    json.dump(pessoa, arquivo_json, indent=2)


print("Terminamos de gravar no arquivo")