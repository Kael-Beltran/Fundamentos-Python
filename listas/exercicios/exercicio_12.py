def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    for nome in notas:
        print(f"O nome da lista é: {nome}")
    return media

lista_de_notas = [7.5, 8.0, 6.5, 9.0, 10.0]

calcular_media(lista_de_notas)