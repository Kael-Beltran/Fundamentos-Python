def remover_produto(produtos, produto):
    produtos.remove(produto)
    for nome in produtos:
        print(f"O nome da lista é: {nome}")
    return produtos

lista_de_comidas = ["Arroz", "Feijão", "Macarrão", "Carne", "Salada"]

remover_produto(lista_de_comidas, "Macarrão")