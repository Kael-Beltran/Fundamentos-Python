def temperatura():
    temp = float(input("Quanto está a temperatura: "))

    if temp < 15:
        print("Frio")
    elif temp <= 25:
        print("Agradável")
    else:
        print("Quente")

temperatura()