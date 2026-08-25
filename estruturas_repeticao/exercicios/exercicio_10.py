def somar_pares():
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: "))

    quantidade = 0
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            quantidade += numero
    return quantidade

resultado = somar_pares()
print(f"A soma dos números pares é: {resultado}")