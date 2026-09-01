def vender_produto(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
    else:
        print("O produto não está disponível.")
    for nome in estoque:
        print(f"O nome da lista é: {nome}")
    return estoque

estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

vender_produto(estoque, "Teclado")