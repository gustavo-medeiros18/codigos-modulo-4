import json

# Causará exceção pois o campo
# numeros_preferidos não poderá
# ser convertido para string JSON

# Sem o campo numeros_preferidos,
# o dict poderá ser convertido
# normalmente.
pessoa = {
    "nome": "Daniel",
    "idade": 50,
    "altura": 1.76,
    "dev": True,
    "linguagens": ["Python", "Java", "Go"],
    "numeros_preferidos": {13, 15, 25}
}

pessoa_json = json.dumps(pessoa, indent=2)
print(type(pessoa_json))
print(pessoa_json)