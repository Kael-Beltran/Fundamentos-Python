def numero():
    num = int(input("Informe um número inteiro: "))

    if num > 0:
        sinal = "positivo"
    elif num < 0:
        sinal = "negativo"
    else:
        sinal = "zero"

    if num % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"

    print(f"Classificação: {sinal} e {paridade}")


numero()