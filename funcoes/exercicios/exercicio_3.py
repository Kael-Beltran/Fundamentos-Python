def numero():
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    resultado = numero1 + numero2
    return resultado

soma = numero()
print(f"O resultado da soma de {soma}!")