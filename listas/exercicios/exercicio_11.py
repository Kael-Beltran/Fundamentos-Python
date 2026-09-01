def somar_numeros(numeros):
    soma = sum(numeros)
    for nome in numeros:
        print(f"O nome da lista é: {nome}")
    return soma

lista_de_numeros = [10, 20, 30, 40, 50]

somar_numeros(lista_de_numeros)