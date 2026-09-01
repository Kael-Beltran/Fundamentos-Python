def adicionar_nome(nomes, nome):
    nomes.append(nome)
    for nome in nomes:
        print(f"O nome da lista é: {nome}")
    return nomes

lista_de_nomes = ["Kael", "Murillo", "Manoel", "Gasque", "Eduardo"]

adicionar_nome(lista_de_nomes, "Beltrão")