def imc():
    altura = float(input("Informe a sua altura (m): "))
    peso = float(input("Informe  seu peso (kg): "))
    imc = peso / (altura * altura)

    if imc <= 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc >= 30:
        print("Obesidade")

imc()