def ingreso():
    idade = int(input("Qual é a sua idade:"))

    if idade == 5:
        print("O valor é gratuito")
    elif idade <=12:
        print("O valor é 10$")
    elif idade <= 59:
        print("O valor é de 20$")
    elif idade >= 60:
        print("O valor é 10$")
    else:
        print("Espere mais alguns messes")

ingreso()