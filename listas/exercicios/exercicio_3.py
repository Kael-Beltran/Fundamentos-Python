def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    for nome in convidados:
        print(f"O nome da lista é: {nome}")
    return convidados

lista_de_nomes = ["Kael", "Murillo", "Manoel", "Gasque", "Eduardo"]
novos = ["Nicolas", "Beltrão"]

adicionar_convidados(lista_de_nomes, novos)