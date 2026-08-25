def fatorial_usuario():
    numero = int(input("Digite um número para calcular o fatorial: "))

    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

resultado = fatorial_usuario()
print(f"O fatorial é: {resultado}")