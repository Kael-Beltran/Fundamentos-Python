def inverter_lista(lista):
    lista_invertida = list(reversed(lista))
    for nome in lista_invertida:
        print(f"O nome da lista é: {nome}")
    return lista_invertida

lista_de_nomes = ["Kael", "Murillo", "Manoel", "Gasque", "Eduardo"]

inverter_lista(lista_de_nomes)