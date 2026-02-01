import random
# from random import random, randint, choice, shuffle

# random() gera números decimais
# (float) aleatórios seguindo o
# intervalo 0 - 1, onde 0 está
# incluso e 1 não.
resultado_random = random.random()
print(f"Valor gerado com random {resultado_random}")

# randint() gera números inteiros
# (int) aleatórios seguindo o
# intervalo definido pelos parâmetros
# (incluindo cada um deles)
resultado_randint = random.randint(20, 30)
print(f"Valor gerado com randint: {resultado_randint}")

minha_lista = ["Brasil", "Inglaterra", "Argentina", "Mexico"]

# choice() escolhe um elemento aleatório a partir
# de uma lista de entrada
elemento_aleatorio = random.choice(minha_lista)
print(f"Elemento da lista selecionado: {elemento_aleatorio}")

for i in range(1, 4):
    elemento_selecionado = random.choice(minha_lista)
    print(f"Elemento {i} selecionado: {elemento_selecionado}")

cartas = ["A", "K", "Q", "J", 10]

# shuffle() altera a ordem na qual os elementos
# de uma lista estão, fazendo isso através
# da modificação da lista original.
print(f"Cartas antes de embaralhar: {cartas}")
random.shuffle(cartas)
print(f"Cartas após embaralhar: {cartas}\n")

for i in range(1, 4):
    random.shuffle(cartas)
    print(f"Embaralhamento {i}: {cartas}")