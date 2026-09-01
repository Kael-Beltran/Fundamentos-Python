def criar_ranking(pontuacoes):
    ranking = sorted(pontuacoes, reverse=True)
    for nome in ranking:
        print(f"O nome da lista é: {nome}")
    return ranking

lista_de_pontuacoes = [150, 320, 80, 450, 210]

criar_ranking(lista_de_pontuacoes)