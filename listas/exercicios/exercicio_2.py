def inserir_aluno(nomes, nome, posicao):
    nomes.insert(posicao, nome)

    for n in nomes:
        print(f"O nome da lista é: {n}")

    return nomes


lista_de_nomes = ["Kael", "Murillo", "Manoel", "Gasque", "Eduardo"]
inserir_aluno(lista_de_nomes, "Nicolas", 2)