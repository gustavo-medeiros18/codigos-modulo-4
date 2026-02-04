from random import choice, shuffle

lista_letras = [
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y",
    "z"
]

lista_numeros = [
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"
]

lista_simbolos = ["!", "@", "#", "$", "%"]

qtd_letras = int(input("Quantas letras você quer na sua senha? "))
qtd_numeros = int(input("Quantos numeros você quer na sua senha? "))
qtd_simbolos = int(input("Quantos simbolos você quer na sua senha? "))

lista_aleatoria = []

for i in range(qtd_letras):
    letra_aleatoria = choice(lista_letras)
    lista_aleatoria.append(letra_aleatoria)

for i in range(qtd_numeros):
    numero_aleatorio = choice(lista_numeros)
    lista_aleatoria.append(numero_aleatorio)

for i in range(qtd_simbolos):
    simbolo_aleatorio = choice(lista_simbolos)
    lista_aleatoria.append(simbolo_aleatorio)

shuffle(lista_aleatoria)

separador = ""
senha_str = separador.join(lista_aleatoria)

print(f"Senha aleatória gerada: {senha_str}")