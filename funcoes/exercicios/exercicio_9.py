def calcular_metro():
    metro = float(input("Digite o valor do metro: "))
    centimetro = metro * 100
    return centimetro

resultado = calcular_metro()
print(f"O seu valor em centimetros é {resultado}!")
