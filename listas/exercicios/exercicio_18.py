def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade if quantidade > 0 else 0
    ordenadas = sorted(temperaturas)

    for nome in ordenadas:
        print(f"O nome da lista é: {nome}")

    return quantidade, soma, media, ordenadas

lista_de_temperaturas = [22.5, 18.0, 30.2, 25.4, 15.8]

analisar_temperaturas(lista_de_temperaturas)