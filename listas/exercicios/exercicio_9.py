def ordenar_nomes(nomes):
    lista_ordenada = sorted(nomes)
    for nome in lista_ordenada:
        print(f"O nome da lista é: {nome}")
    return lista_ordenada

lista_de_nomes = ["Kael", "Murillo", "Manoel", "Gasque", "Eduardo"]

ordenar_nomes(lista_de_nomes)