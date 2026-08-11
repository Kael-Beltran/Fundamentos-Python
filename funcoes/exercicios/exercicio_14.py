def viagem():
    distancia = float(input("Quantos KM você iria fazer na viagem: "))
    combustivel = float(input("Quantos litros de gasolina você vai por: "))
    media_litros = distancia / combustivel
    preco = combustivel * 6.45
    return media_litros, preco

media_por_litros, preco = viagem()
print(f"A media de combustivel do seu carro é {media_por_litros:.2f}, ficou em {preco:.2f}")
