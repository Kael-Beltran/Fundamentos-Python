def frete():
    valor = float(input("Informe o valor da compra: "))

    if valor <= 100:
        total = valor + 20
        print(f"O valor do frete é R$ 20. Total: R$ {total}")
    elif valor <= 300:
        total = valor + 10
        print(f"O valor do frete é R$ 10. Total: R$ {total}")
    else:
        print(f"Frete grátis! Total: R$ {valor}")

frete()