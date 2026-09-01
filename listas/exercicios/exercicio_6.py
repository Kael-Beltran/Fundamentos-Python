def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)
    for nome in produtos:
        print(f"O nome da lista é: {nome}")
    return posicao

lista_de_comidas = ["Arroz", "Feijão", "Macarrão", "Carne", "Salada"]

encontrar_produto(lista_de_comidas, "Carne")