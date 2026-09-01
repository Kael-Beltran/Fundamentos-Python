def remover_item(itens, posicao):
    item_removido = itens.pop(posicao)
    for nome in itens:
        print(f"O nome da lista é: {nome}")
    return item_removido

lista_de_comidas = ["Arroz", "Feijão", "Macarrão", "Carne", "Salada"]

remover_item(lista_de_comidas, 2)