def troca():
    valor1 = float(input("Digite o valor do A: "))
    valor2 = float(input("Digite o valor do B: "))
    valorA = valor1 = valor2
    valorB = valor2 = valor1
    return valor3, valor4

valor1, valor2 = troca()
print(f"O valor A agora é {valor1} e o valor B agora é {valor2}")