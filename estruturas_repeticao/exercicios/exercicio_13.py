def mostrar_primos_usuario():
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: "))

    print(f"\nNúmeros primos entre {inicio} e {fim}:")

    for numero in range(inicio, fim + 1):
        if numero > 1:
            eh_primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    eh_primo = False
                    break

            if eh_primo:
                print(numero)

mostrar_primos_usuario()