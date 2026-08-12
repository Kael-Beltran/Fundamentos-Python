def numeros():
    numero1 = float(input("Qual seu numero:"))
    numero2 = float(input("Qual é o segundo numero:"))

    if numero1 == numero2:
        print("Os números são iguais!")
    elif numero1 > numero2:
        print(f" {numero1} é maior que {numero2}")
    else:
        print(f" {numero2} é maior que {numero1}")

numeros()