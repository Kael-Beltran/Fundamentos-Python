def votacao():
    idade = int(input("Qual é a sua idade: "))

    if idade < 16:
        print("Não pode votar")
    elif idade < 18 or idade >= 70:
        print("Voto opcional")
    else:
        print("Voto obrigatório")

votacao()