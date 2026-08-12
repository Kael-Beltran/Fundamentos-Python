def calculadora():
    operacao = input("Selecione a sua operacao [+], [-], [*], [/]\n")
    numero1 = int(input("Informe o primeiro numero: "))
    numero2 = int(input("Informe o segundo numero: "))

    if operacao == "+":
        print(numero1 + numero2)
    elif operacao == "-":
        print(numero1 - numero2)
    elif operacao == "*":
        print(numero1 * numero2)
    elif operacao == "/":
        print(numero1 / numero2)
    else:
        print("Operacao invalida")

calculadora()