def maior_numero():
    maior = float(input("Digite um número: "))

    while True:
        continuar = input("Quer digitar outro número? (s/n): ")

        if continuar != 's':
            break

        numero = float(input("Digite outro número: "))

        if numero > maior:
            maior = numero
    return maior

resultado = maior_numero()
print(f"O maior número foi: {resultado}")