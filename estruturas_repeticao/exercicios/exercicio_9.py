def contar_pares_usuario():
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: "))

    quantidade = 0
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            quantidade += 1

    return quantidade

resultado = contar_pares_usuario()
print(f"Quantidade de números pares: {resultado}")