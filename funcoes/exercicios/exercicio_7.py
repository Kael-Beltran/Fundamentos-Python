def area_retangulo():
    base = float(input("Digite o valor do primeiro numero: "))
    altura = float(input("Digite o valor do segundo numero: "))
    area = base * altura
    return area

area = area_retangulo()
print(f"A área do retangulo é {area}!")