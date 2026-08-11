def compras():
    produto = float(input("Digite o valor do produto: "))
    desconto = float(input("Digite a porcentagem de desconto: "))
    valor_desconto = (produto * desconto) / 100
    valor_final = produto - valor_desconto
    return produto, valor_final

preco_original, preco_final = compras()
print(f"O produto de R$ {preco_original:.2f} com desconto ficou R$ {preco_final:.2f}!")