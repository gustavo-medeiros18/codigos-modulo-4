import json

pessoa = {
    "nome": "Gustavo",
    "idade": 20,
    "email": "gustavo@cdc.com",
    "desenvolvedor": True
}

print(pessoa["email"])

print(f"Tipo da pessoa: {type(pessoa)}\n")
json_equivalente = json.dumps(pessoa, indent=2)

print(repr(json_equivalente))
print(f"Tipo do json equivalente (conversão): {type(json_equivalente)}")
