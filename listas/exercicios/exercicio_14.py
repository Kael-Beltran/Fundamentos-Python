def adicionar_produtos(compras, produtos):
    compras.extend(produtos)
    for nome in compras:
        print(f"O nome da lista é: {nome}")
    return compras

def cancelar_compra(compras, produto):
    compras.remove(produto)
    for nome in compras:
        print(f"O nome da lista é: {nome}")
    return compras

lista_de_compras = ["Arroz", "Feijão", "Macarrão"]
novos_produtos = ["Carne", "Salada"]

adicionar_produtos(lista_de_compras, novos_produtos)
cancelar_compra(lista_de_compras, "Macarrão")