def perimetro_retangulo():
    base = int(input("Digite o valor do primeiro numero: "))
    altura = int(input("Digite o valor do segundo numero: "))
    perimetro = (base + altura) * 2
    return perimetro

soma = perimetro_retangulo()
print(f"O perimetro do retângulo é {soma}!")
