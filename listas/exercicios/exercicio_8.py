def ordenar_numeros(numeros):
    lista_ordenada = sorted(numeros)
    for nome in lista_ordenada:
        print(f"O nome da lista é: {nome}")
    return lista_ordenada

lista_de_numeros = [15, 3, 42, 8, 23, 1]

ordenar_numeros(lista_de_numeros)