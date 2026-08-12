def notas():
    nota = float(input("Qual sua nota: "))

    if nota < 0 or nota > 10:
        print("Valor invalido!")
    elif nota < 5:
        print("Insuficiente!")
    elif nota < 7:
        print("Regular!")
    elif nota < 9:
        print("Bom!")
    else:
        print("Excelente!")


notas()