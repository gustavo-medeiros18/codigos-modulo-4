lista_caracteres = ["C", "D", "C"]

# Um jeito de formar uma string a partir
# de uma lista de caracteres: usando a
# função (método) join, onde o separador
# pode ser uma string vazia para que os
# caracteres, na prática, não fiquem 
# separados, mas sim, "colados" uns nos
# outros:
separador = ""
string_resultante = separador.join(lista_caracteres)

tipo_resultante = type(string_resultante)
print(f"String resultante: {string_resultante}")
print(f"Tipo da string resultante: {tipo_resultante}")