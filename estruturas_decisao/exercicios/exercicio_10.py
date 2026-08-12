def desconto():
    valor = float(input("Informe o valor do produto: "))

    if valor <= 0:
        print("O valor do produto deve ser positivo!")
    elif valor <= 100:
        print("O produto não recebe desconto!")
    elif valor <= 500:
        valor_com_desconto = valor * 0.90
        print(f"O produto recebeu 10% de desconto e ficou por R$ {valor_com_desconto:.2f}")
    else:
        valor_com_desconto = valor * 0.85
        print(f"O produto recebeu 15% de desconto e ficou por R$ {valor_com_desconto:.2f}")

desconto()