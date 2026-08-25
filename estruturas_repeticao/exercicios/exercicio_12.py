def eh_primo():
    numero = int(input("Digite um numero para saber se é primo ou não: "))

    if numero <= 1:
        return numero, False

    for i in range(2, numero):
        if numero % i == 0:
            return numero, False

    return numero, True


num, resultado = eh_primo()

if resultado:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} NÃO é primo!")