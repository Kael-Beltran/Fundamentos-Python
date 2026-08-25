def mostrar_impares():
    numero = int(input("Digite um número limite: "))

    for i in range(numero + 1):
        if i % 2 == 1:
            print(i)

mostrar_impares()